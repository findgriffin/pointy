from formcreator import Form, Doc, Text, Boolean
import utils
import datetime

def history(begin=None, end=None, week=False, month=False):
    if week or month:
        end = datetime.datetime.now()
        if week:
            begin = end - datetime.timedelta(days=7)
        if month:
            begin = end - datetime.timedelta(days=28)
    else:
        try:
            begin = utils.parse_date(begin, dtime=True)
        except ValueError:
            return 'Error: unable to parse date %s' % begin
        try:
            end = utils.parse_date(end, dtime=True)
        except ValueError:
            return 'Error: unable to parse date %s' % end
    cd = utils.compose_date
    if not begin <= end:
        return 'Error: %s is not before %s' % (cd(begin), cd(end))
    db = utils.read_db()
    days = [utils.compose_date(begin + datetime.timedelta(days=x)) for x in xrange(0,
        (end-begin).days)]
    matches = ['from: %s to: %s' % (cd(begin), cd(end))]
    for day in days:
        matches.append('%s: %s' % (day, utils.daily_points(day, db)))

    return '\n'.join(matches)
history_form = Form(history, inline=True)#, output_type='html')
history_form += Doc("""
Select a range of days to view. Or select the last week / four weeks.
""")
history_form += Text('', name='begin', cmd_opt='begin', default=utils.today)
history_form += Text('', name='end', cmd_opt='end', default=utils.today)
history_form += Boolean("last week", cmd_opt="week")
history_form += Boolean("last four weeks", cmd_opt="month")
