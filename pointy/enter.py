""" The pointy app, using formcreator."""
from formcreator import Form, MainApp, Text, Integer, Doc, TextArea
import datetime

def enter_food(date, breakfast, breakfast_pts, lunch, lunch_pts, dinner,
        dinner_pts, snacks, snack_pts, hi):
    with open('enter.out', 'wb') as fp:
        fp.write('%s %s %s' % (breakfast, lunch, dinner))

def enter_training(workout):
    with open('enter.out', 'wb') as fp:
        fp.write('workout:\n%s' % workout)

food = Form(enter_food, name="Food")
now = datetime.datetime.now()
today = '%s/%s/%s' % (now.day, now.month, now.year)

food += Text('Date', default=today)
food += Doc("""
Enter food1 [points], food2 [points],... in the fields below. Points may be
ommitted if the food has been seen before.
""")
food += Text('Breakfast')
food += Text('Lunch')
food += Text('Dinner')
food += Text('Snacks')

train = Form(enter_training, name="Train")
train += Text('Date', default=today)
train += TextArea('Workout')
pointy_app = MainApp('Pointy', [food, train])
pointy_app.run()


