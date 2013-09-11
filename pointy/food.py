""" Calculate the points for various food items."""

TABLE = {
#   "item": (breakfast, lunch, dinner, snack)
    "upngo":           (1,      0,      0,      None),
    "omlette":         (2,      2,      2,      None),
    "pronto:wrap":     (2,      2,      0,      None),
    "bigbreakfast":    (1,      2,      1,      None),
    "none":            (0,      -1,     -2,     None),
    "pronto:small":    (None,   2,      None,   None),
    "pronto:large":    (None,   1,      None,   None),
    "mcdonalds":       (-5,     -3,     -3,     None),
    "mexican":         (-1,     2,      3,      None),
    "burger":          (-1,     1,      2,      None),
    "pizza:medium":    (None,   1,      2       None),
    "pizza:large":     (None,   0,      1,      None),
    "kebab": 1,
    "coke": (0,0,0,-1),
    }
ORDER = ['breakfast', 'lunch', 'dinner', 'snack']
def points(item, meal, home=False):
    extras = 0
    if home:
        extras += 1
        
    if not meal in ORDER:
        raise ValueError('%s is not a valid meal time' % meal)
    if not item in TABLE:
        raise ValueError('Unknown food: %s' % item)
    return TABLE[item][ORDER.index(meal)] + extras

