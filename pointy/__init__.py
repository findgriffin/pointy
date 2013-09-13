from formcreator import MainApp 
from food import food
from train import train

app = MainApp('Pointy', [food, train])

def run():
    app.run()

if __name__ == "__main__":
    run()