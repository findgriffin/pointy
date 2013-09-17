from formcreator import Form, Text, TextArea
import utils

def training(date=None, workout=None):
    return 'on %s workout:\n%s' % (date, workout)

train = Form(training)
train += Text('Date', default=utils.today, cmd_opt='date')
train += TextArea('Workout', cmd_opt='workout')
