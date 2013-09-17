from formcreator import Form, Text, TextArea
import utils

def training(date=None, workout=None):
    return 'on %s workout:\n%s' % (date, workout)

train_form = Form(training)
train_form += Text('Date', default=utils.today, cmd_opt='date')
train_form += TextArea('Workout', cmd_opt='workout')
