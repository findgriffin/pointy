""" The pointy app, using formcreator."""
from formcreator import Form, MainApp, Text, Integer
import datetime

def enter_food(breakfast, lunch, dinner, snacks, date):
    with open('enter.out', 'wb') as fp:
        fp.write('%s %s %s' % (breakfast, lunch, dinner))

def enter_training(workout):
    with open('enter.out', 'wb') as fp:
        fp.write('workout:\n%s' % workout)

food = Form(enter_food, name="Food")
now = datetime.datetime.now()
today = '%s/%s/%s' % (now.day, now.month, now.year)

food += Text('Date', default=today)
food += Text('Breakfast')
food += Integer('breakfast_points')
food += Text('Lunch')
food += Integer('lunch_points')
food += Text('Dinner')
food += Integer('dinner_points')
food += Text('Snacks')
food += Integer('snack_points')

train = Form(enter_training, name="Train")
train += Text('Workout')
pointy_app = MainApp('Pointy', [food, train])
pointy_app.run()


