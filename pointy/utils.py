import os
import json
import datetime

now = datetime.datetime.now()
today = '%s/%s/%s' % (now.day, now.month, now.year)

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
