

class Food:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class Herbivore:
    def eat(self, food):
        if food.type == "plant":
            print(f"{food.name} is plant-based, I will eat.")
        else:
            super().eat(food)
class Carnivore:
    def eat(self, food):
        if food.type == "animal":
            print(f"{food.name} is animal-based, I will eat.")
        else:
            print(f"No u.")
class Rat(Herbivore, Carnivore):
    pass

rat = Rat()

grass = Food("grass", "plant")
rat.eat(grass)
rat.eat(Food("ant", "animal"))