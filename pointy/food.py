""" Calculate the points for various food items."""
        
from formcreator import Form, Text, Doc
import utils
from dateutil import parser

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
        dtime = parser.parse(date, dayfirst=True)
    except ValueError:
        return 'ERROR: unable to process date: %s'
    date = dtime.strftime('%d/%m/%Y')
    db = utils.read_database()
    initial = utils.daily_points(date, db)
    messages = ['%s had %s points' % (date, initial)]
    messages.extend(process_meal(breakfast, db, date, 'breakfast'))
    messages.extend(process_meal(lunch, db, date, 'lunch'))
    messages.extend(process_meal(dinner, db, date, 'dinner'))
    messages.extend(process_meal(snacks, db, date, 'snacks'))
    final = utils.daily_points(date, db)
    diff = final - initial
    messages.append('%s added %s points (now has %s)' % (date, diff, final))
    utils.write_database(db)
    return '\n'.join(messages)
    

food = Form(enter_food, name="Food")#, output_type='markdown')

food += Text('Date', name='date', default=utils.today)
food += Doc("""
Enter food1 [points], food2 [points],... in the fields below. Points may be
ommitted if the food has been seen before.
""")
food += Text('Breakfast', cmd_opt='breakfast')
food += Text('Lunch', cmd_opt='lunch')
food += Text('Dinner', cmd_opt='dinner')
food += Text('Snacks', cmd_opt='snacks')
