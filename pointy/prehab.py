""" Record prehab exercises, stretches, massage etc."""
from formcreator import Form, Text, TextArea
import utils

def process_loc(text, db, date, name):
    messages = ['%s: ' % name]
    for part in text.split(','):
        try:
            name, points, msg = utils.process_item(part, db['prehab']) 
        except ValueError as err:
            messages[-1] += err.message

        else:
            if not date in db['days']:
                db['days'][date] = []
            db['days'][date].append((name, points))
            messages.append(msg)
    return messages

def prehab(date=None, home=None, work=None, travel=None, other=None):
    try:
        date = utils.parse_date(date)
    except ValueError:
        return 'Error: unable to parse date %s' % date
    db = utils.read_db()
    initial = utils.daily_points(date, db)
    messages = ['%s had %s points' % (date, initial)]
    messages.extend(process_loc(home, db, date, 'home'))
    messages.extend(process_loc(work, db, date, 'work'))
    messages.extend(process_loc(travel, db, date, 'travel'))
    messages.extend(process_loc(other, db, date, 'other'))
    final = utils.daily_points(date, db)
    diff = final - initial
    messages.append('%s added %s points (now has %s)' % (date, diff, final))
    utils.write_db(db)
    return '\n'.join(messages)
        


prehab = Form(prehab)
prehab += Text('Date', default=utils.today, cmd_opt='date')
prehab += TextArea('Home', cmd_opt='home')
prehab += TextArea('Work', cmd_opt='work')
prehab += TextArea('Travel', cmd_opt='travel')
prehab += TextArea('Other', cmd_opt='other')
