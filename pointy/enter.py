""" The pointy app, using formcreator."""
from formcreator import Form, MainApp, Text, Integer, Doc, TextArea
from dateutil import parser

import json
import datetime
import os

def read_database(location='pointy.json'):
    if not os.path.exists(location):
        return {'days': {}, 'foods': {}}
    with open(location, 'rb') as db:
        return json.load(db)

def write_database(data, location='pointy.json'):
    with open(location, 'wb') as db:
        db.write(json.dumps(data, indent=4))

def is_point_value(item):
    if item.startswith('-'):
        item = item[1:]
    return item.isdigit()

def process_item(item, items):
    if not item:
        raise ValueError('blank item')
    parts = item.split()
    if is_point_value(parts[-1]):
        points = int(parts[-1])
        item = ' '.join(parts[:-1])
        items[item] = points
        message = '%s updated with points value %s' % (item, points)
        return item, points, message
    elif item in items:
        message = 'used previous points %s for %s' % (items[item], item)
        return item, items[item], message
    else:
        raise ValueError('could not determine points for %s' % item)

def daily_points(date, db):
    total = 0
    if date in db['days']:
        for val in db['days'][date]:
            total += val[1]
    return total

        
def process_meal(text, db, date, name):
    messages = ['%s: ' % name]
    for part in text.split(','):
        try:
            name, points, msg = process_item(part, db['foods']) 
        except ValueError as err:
            messages[-1] += err.message

        else:
            if not date in db['days']:
                db['days'][date] = []
            db['days'][date].append((name, points))
            messages.append(msg)
    return messages

def enter_food(date, breakfast=None, lunch=None, dinner=None, snacks=None):
    
    try:
        dtime = parser.parse(date, dayfirst=True)
    except ValueError:
        return 'ERROR: unable to process date: %s'
    date = dtime.strftime('%d/%m/%Y')
    db = read_database()
    initial = daily_points(date, db)
    messages = ['%s had %s points' % (date, initial)]
    messages.extend(process_meal(breakfast, db, date, 'breakfast'))
    messages.extend(process_meal(lunch, db, date, 'lunch'))
    messages.extend(process_meal(dinner, db, date, 'dinner'))
    messages.extend(process_meal(snacks, db, date, 'snacks'))
    final = daily_points(date, db)
    diff = final - initial
    messages.append('%s added %s points (now has %s)' % (date, diff, final))
    write_database(db)
    return '\n'.join(messages)
    
def enter_training(workout):
    with open('enter.out', 'wb') as fp:
        fp.write('workout:\n%s' % workout)

food = Form(enter_food, name="Food")#, output_type='markdown')
now = datetime.datetime.now()
today = '%s/%s/%s' % (now.day, now.month, now.year)

food += Text('Date', name='date', default=today)
food += Doc("""
Enter food1 [points], food2 [points],... in the fields below. Points may be
ommitted if the food has been seen before.
""")
food += Text('Breakfast', cmd_opt='breakfast')
food += Text('Lunch', cmd_opt='lunch')
food += Text('Dinner', cmd_opt='dinner')
food += Text('Snacks', cmd_opt='snacks')

train = Form(enter_training, name="Train")
train += Text('Date', default=today)
train += TextArea('Workout')
pointy_app = MainApp('Pointy', [food, train])
pointy_app.run()


