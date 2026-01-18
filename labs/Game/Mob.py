from random import *

mobs = ['Гоблин','Гном',"Таракан","Зомби","Скелет","Пират","Призрак","Скелет-лучник","Гоблин-вор","Неоднородная масса","Огр","НИКИТОС"]

class Mob:
    def __init__(self,mob_lvl,room):
        self.name = ''
        self.max_hp = 0
        self.cur_hp = 0
        self.strenght = 0
        self.agility = 0
        self.defence = 0
        self.floor = mob_lvl
        self.room = room
        self.exp = 0

    def mob_stats(self):
        rand_num = randint(0,100)

        if 0 <= rand_num < 10:
            self.name = "Гоблин"
            self.max_hp = 10
            self.strenght = 5
            self.agility = 1
            self.defence = 2

        elif 10 <= rand_num < 20:
            self.name = "Гном"
            self.max_hp = 10
            self.strenght = 3
            self.agility = 3
            self.defence = 2

        elif 20 <= rand_num < 30:
            self.name = "Таракан"
            self.max_hp = 5
            self.strenght = 3
            self.agility = 5
            self.defence = 1

        elif 30 <= rand_num < 40:
            self.name = "Зомби"
            self.max_hp = 20
            self.strenght = 3
            self.agility = 1
            self.defence = 2

        elif 40 <= rand_num < 50:
            self.name = "Скелет"
            self.max_hp = 15
            self.strenght = 5
            self.agility = 1
            self.defence = 1

        elif 50 <= rand_num < 60:
            self.name = "Пират"
            self.max_hp = 8
            self.strenght = 7
            self.agility = 3
            self.defence = 1

        elif 60 <= rand_num < 70:
            self.name = "Призрак"
            self.max_hp = 10
            self.strenght = 3
            self.agility = 3
            self.defence = 1

        elif 70 <= rand_num < 80:
            self.name = "Скелет-лучник"
            self.max_hp = 15
            self.strenght = 3
            self.agility = 3
            self.defence = 1

        elif 80 <= rand_num < 90:
            self.name = "Гоблин-вор"
            self.max_hp = 10
            self.strenght = 5
            self.agility = 1
            self.defence = 2

        elif 90 <= rand_num < 95:
            self.name = "Неоднородная масса"
            self.max_hp = 30
            self.strenght = 10
            self.agility = 3
            self.defence = 4

        elif 95 <= rand_num < 98:
            self.name = "Огр"
            self.max_hp = 50
            self.strenght = 10
            self.agility = 0
            self.defence = 3

        else:
            self.name = "НИКИТОС"
            self.max_hp = 100
            self.strenght = 5
            self.agility = 1
            self.defence = 5

        self.cur_hp = self.max_hp
    
    def mob_scale(self):
        self.mob_stats()

        for j in range(2):
            for i in range(self.room):
                rand_num = randint(1,4)

                if rand_num == 1:
                    self.max_hp += 2
                    self.cur_hp += 2

                elif rand_num == 2:
                    self.strenght += 1

                elif rand_num == 3:
                    self.defence += 1

                else:
                    self.agility += 1

        for i in range(self.floor - 1):
            self.max_hp += 2
            self.cur_hp += 2
            self.strenght += 1
            self.defence += 1
            self.agility += 1
            
    def mob_show_stats(self):
        self.mob_scale()
        self.mob_exp()

        print('ВАШ ВРАГ:')
        print('---------')
        print(f'Name:{self.name}')
        print('---------')
        print(f'HP:{self.cur_hp}\{self.max_hp}')
        print(f'STR:{self.strenght}')
        print(f'AGI:{self.agility}')
        print(f'DEF:{self.defence}') 
        print('---------')
        return self.cur_hp, self.max_hp, self.strenght, self.agility, self.defence, self.exp
    
    def mob_exp(self):
        if self.name in mobs[:9]:
            self.exp = 3 * self.floor

        elif self.name in mobs[9:][:1]:
            self.exp = 10 * self.floor

        elif self.name in mobs[10:]:
            self.exp = 20 * self.floor