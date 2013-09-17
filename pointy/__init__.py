from formcreator import MainApp 
from food import food_form
from prehab import prehab_form
from foods import foods_form
from train import train_form
from history import history_form

def getapp(port=5000, host='127.0.0.1', not_public=True):
    return MainApp('Pointy', [food_form, train_form, prehab_form, history_form,
        foods_form], port=port, host=host, not_public=not_public)

