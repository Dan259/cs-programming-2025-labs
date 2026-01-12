from random import *

class Character:
    def __init__(self,name,race):
        self._name = name
        self._race = race

    def char_stats(self):
        if self._race == "Человек":
            hp = randint(90,110)
            strenght = randint(4,8)
            agility = randint(5,10)
            defence = randint(3,5)
            height = randint(150,200)
            weight = randint(60,90)
            if weight < 70 and height < 160:
                strenght -= 1
                agility += 1
            elif weight > 80 and height > 190:
                strenght += 1
                agility -= 1
        elif self._race == "Эльф":
            hp = randint(70,90)
            strenght = randint(4,8)
            agility = randint(8,14)
            defence = randint(3,5)
            height = randint(175,210)
            weight = randint(40,70)
            if weight < 50 and height < 185:
                strenght -= 1
                agility += 2
            elif weight > 60 and height > 200:
                strenght += 1
                agility -= 1
        elif self._race == "Дворф":
            hp = randint(100,130)
            strenght = randint(5,10)
            agility = randint(3,6)
            defence = randint(6,10)
            height = randint(100,130)
            weight = randint(70,100)
            if weight < 80 and height < 110:
                strenght -= 1
                agility += 1
            elif weight > 90 and height > 120:
                strenght += 2
                agility -= 1
        else:
            print("Выбирай из того, что есть")
        return hp, strenght, agility, defence, height, weight
        