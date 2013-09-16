from formcreator import Form, Doc, Text
import utils

def history(begin, end):
    try:
        begin = utils.parse_date(begin)
    except ValueError:
        return 'Error: unable to parse date %s' % begin
    try:
        end = utils.parse_date(end)
    except ValueError:
        return 'Error: unable to parse date %s' % end

    return "from: %s to: %s" % (begin, end)
history = Form(history, inline=True, output_type='html')
history += Doc("""
Select a range of days to view.
""")
history += Text('', name='begin', default=utils.today)
history += Text('', name='end', default=utils.today)
