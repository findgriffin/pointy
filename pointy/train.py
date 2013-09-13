from formcreator import Form, Text, TextArea
import utils

def enter_training(workout):
    with open('enter.out', 'wb') as fp:
        fp.write('workout:\n%s' % workout)

train = Form(enter_training, name="Train")
train += Text('Date', default=utils.today)
train += TextArea('Workout')
