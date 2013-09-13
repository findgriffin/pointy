from formcreator import MainApp 
from food import food
from foods import foods
from train import train

app = MainApp('Pointy', [food, train, foods])

def run():
    app.run()

if __name__ == "__main__":
    run()
