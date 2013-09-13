from formcreator import MainApp 
from food import food
from prehab import prehab
from foods import foods
from train import train

def getapp(port=5000, host='127.0.0.1', not_public=True):
    return MainApp('Pointy', [food, train, prehab, foods], port=port,
            host=host, not_public=not_public)

