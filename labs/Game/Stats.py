from random import *

items = [['Меч','Кинжал','Лук','Копье','Сковородочаки'],['Латная броня','Кольчуга','Кожаная броня'],['Зелье здоровья(Маленькое)','Зелье здоровья(Среднее)','Зелье здоровья(Большое)']]
max_hp, cur_hp, strenght, agility, defence, money = 0, 0, 0, 0, 0, 0
inventory = ["Хуй","Залупа","Член"]


class Character:
    def __init__(self):
        print('Who are you?')
        name = input("> ")
        print("Выберите расу:")
        print("1 - Человек")
        print("2 - Эльф")
        print("3 - Дворф")
        race = input('> ')
        print("Ваш персонаж создан!")
        self._name = name
        self._race = race

    def char_stats(self):
        global max_hp, cur_hp, strenght, agility, defence
        if self._race == "1":
            max_hp = randint(90,110)
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
        elif self._race == "2":
            max_hp = randint(70,90)
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
        elif self._race == "3":
            max_hp = randint(100,130)
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
            print("Такой расы нет!")
        cur_hp = max_hp
        return max_hp, strenght, agility, defence, height, weight
    
    def show_stats(self,lvl,exp,req_exp):
        global max_hp, cur_hp, strenght, agility, defence
        print('ВАШ ПЕРСОНАЖ:')
        print('---------')
        print(f'Name:{self._name}')
        print('---------')
        print(f'LVL:{lvl}')
        print(f'EXP:{exp}\{req_exp}')
        print('---------')
        print(f'HP:{cur_hp}\{max_hp}')
        print(f'STR:{strenght}')
        print(f'AGI:{agility}')
        print(f'DEF:{defence}') 
        print('---------')

    def up_stats(self):
        global max_hp, strenght, agility, defence
        print("Выберите характеристику:")
        print("1 - +2 к HP")
        print("2 - +1 к атаке")
        print("3 - +1 к ловкости")
        print("4 - +1 к броне")
        num_up = input('> ')
        if num_up == "1":
            max_hp += 2
        elif num_up == "2":
            strenght += 1
        elif num_up == "3":
            agility += 1
        elif num_up == "4":
            defence += 1
        else:
            print("Такой опции нет")
    
    def show_inventory(self):
        global inventory
        for i in range(len(inventory)):
            print(f'{i+1} - {inventory[i]}')