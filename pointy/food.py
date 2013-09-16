""" Calculate the points for various food items."""
        
from formcreator import Form, Text, Doc
import utils

def process_meal(text, db, date, name):
    messages = ['%s: ' % name]
    for part in text.split(','):
        try:
            name, points, msg = utils.process_item(part, db['foods']) 
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
        date = utils.parse_date(date)
    except ValueError:
        return 'Error: unable to parse date %s' % date
    db = utils.read_db()
    initial = utils.daily_points(date, db)
    messages = ['%s had %s points' % (date, initial)]
    messages.extend(process_meal(breakfast, db, date, 'breakfast'))
    messages.extend(process_meal(lunch, db, date, 'lunch'))
    messages.extend(process_meal(dinner, db, date, 'dinner'))
    messages.extend(process_meal(snacks, db, date, 'snacks'))
    final = utils.daily_points(date, db)
    diff = final - initial
    messages.append('%s added %s points (now has %s)' % (date, diff, final))
    utils.write_db(db)
    return '\n'.join(messages)
    

food = Form(enter_food, name="Food")

food += Text('Date', name='date', default=utils.today)
food += Doc("""
Enter food1 [points], food2 [points],... in the fields below. Points may be
ommitted if the food has been seen before.
""")
food += Text('Breakfast', cmd_opt='breakfast')
food += Text('Lunch', cmd_opt='lunch')
food += Text('Dinner', cmd_opt='dinner')
food += Text('Snacks', cmd_opt='snacks')
