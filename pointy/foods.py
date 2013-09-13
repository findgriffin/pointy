""" Adjust the points value of different foods."""
from formcreator import Form, Text
import utils
db = utils.read_db()
foods_db = db['foods']
def change_foods(**kwargs):
    msg = []
    change_count = 0
    for key, val in kwargs.items():
        val = val.lstrip(key).strip()
        if not utils.is_point_value(val):
            msg.append('%s: %s is not valid' % (key, val))
            continue
        val_int = int(val)
        if val_int == foods_db[key]:
            continue
        original = foods_db[key]
        foods_db[key] = val_int
        msg.append('%s changed from %s to %s' % (key, original, val_int))
        change_count += 1
    utils.write_db(db)
    msg.append('changed %s of %s items' % (change_count, len(kwargs)))
    return '\n'.join(msg)
foods = Form(change_foods, name='Foods')

for food, points in foods_db.items():
    foods += Text('', default='%s %s' % (food, points), cmd_opt=food)
