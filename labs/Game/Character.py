from random import *
from Mob import *

items = [['Меч','Кинжал','Лук','Копье','Сковородочаки'],['Латная броня','Кольчуга','Кожаная броня'],
         ['Зелье здоровья(Маленькое)','Зелье здоровья(Среднее)','Зелье здоровья(Большое)']]
inventory = {'Weapon':'','Armor':''}
for i in range(1,6): inventory[str(i)] = ''

class Character:
    def __init__(self):
        print('\nWho are you?\n')
        self.name = input("> ")
        self.race = ''
        self.max_hp = 0
        self.cur_hp = 0
        self.strenght = 0
        self.agility = 0
        self.defence = 0
        self.money = 0
        self.floor = 0
        self.exp = 0
        self.req_exp = 5
        self.lvl = 1
        self.stat_point = 0
        self.height = 0
        self.weight = 0
        self.room = 0

    def char_stats(self):
        print("\nВыберите расу:")
        print("1 - Человек")
        print("2 - Эльф")
        print("3 - Дворф\n")
        self.race = input("> ")

        # Создание человека
        if self.race == "1":
            self.max_hp = randint(80,100)
            self.strenght = randint(4,8)
            self.agility = randint(5,10)
            self.defence = randint(1,3)
            self.height = randint(150,200)
            self.weight = randint(60,90)

            # Изменение характеристик в зависимости от веса
            if self.weight < 70 and self.height < 160:
                self.strenght -= 1
                self.agility += 1

            # Изменение характеристик в зависимости от роста
            elif self.weight > 80 and self.height > 190:
                self.strenght += 1
                self.agility -= 1

            print("\nВаш персонаж создан!")
            
        # Создание эльфа
        elif self.race == "2":
            self.max_hp = randint(70,90)
            self.strenght = randint(4,8)
            self.agility = randint(7,13)
            self.defence = randint(1,3)
            self.height = randint(175,210)
            self.weight = randint(40,70)

            # Изменение характеристик в зависимости от веса
            if self.weight < 50 and self.height < 185:
                self.strenght -= 1
                self.agility += 2

            # Изменение характеристик в зависимости от роста
            elif self.weight > 60 and self.height > 200:
                self.strenght += 1
                self.agility -= 1

            print("\nВаш персонаж создан!")

        # Создание дворфа
        elif self.race == "3":
            self.max_hp = randint(100,130)
            self.strenght = randint(5,10)
            self.agility = randint(2,4)
            self.defence = randint(3,5)
            self.height = randint(100,130)
            self.weight = randint(70,100)

            # Изменение характеристик в зависимости от веса
            if self.weight < 80 and self.height < 110:
                self.strenght -= 1
                self.agility += 1

            # Изменение характеристик в зависимости от роста
            elif self.weight > 90 and self.height > 120:
                self.strenght += 2
                self.agility -= 1

            print("\nВаш персонаж создан!")

        else:
            print("Такой расы нет!")
            self.char_stats()

        self.cur_hp = self.max_hp
    
    def show_stats(self):
        print('\nВАШ ПЕРСОНАЖ:')
        print('----------')
        print(f'Name:{self.name}')
        print('----------')
        print(f'LVL:{self.lvl}')
        print(f'EXP:{self.exp}\{self.req_exp}')
        print('----------')
        print(f'HP:{self.cur_hp}\{self.max_hp}')
        print(f'STR:{self.strenght}')
        print(f'AGI:{self.agility}')
        print(f'DEF:{self.defence}') 
        print('----------')

    def up_stats(self):
        while self.stat_point > 0:
            print("\nВыберите характеристику:\n1 - +2 к HP\n2 - +1 к атаке\n3 - +1 к ловкости\n4 - +1 к броне\n")
            num_up = input('> ')

            if num_up == "1":
                self.max_hp += 2
                self.cur_hp += 2
                self.stat_point -= 1

            elif num_up == "2":
                self.strenght += 1
                self.stat_point -= 1

            elif num_up == "3":
                self.agility += 1
                self.stat_point -= 1

            elif num_up == "4":
                self.defence += 1
                self.stat_point -= 1

            else:
                print("Такой опции нет")
    
    def show_inventory(self):
        global inventory

        # Показывает слот оружия и брони
        print(f'\nВаш инвентарь:\nWeapon - {inventory['Weapon']}\nArmor - {inventory['Armor']}')

        # Показывает слоты инвенторя
        for i in range(1,6):
            print(f'{i} - {inventory[str(i)]}')

        # Показывает деньги
        print(f'Money - {self.money}')

    def add_in_inventory(self,add_item):
        global inventory

        # Добавление предмета, если в инвентаре есть свободная ячейка
        for i in range(1,6):
            if inventory[str(i)] == '':
                inventory[str(i)] = add_item
                break

        # Добавление предмета, если инвентарь заполнен
        else:
            print('Ваш инвентарь заполнен.\nЧто вы будете делать?\n1 - Выбросить что-то из инвентаря\n2 - Не подбирать вещь')
            chosen_num = input('> ')

            if chosen_num == '1':
                print('\nВыберите вещь, которую выкинете:\n')

                for j in range(1,6):
                    print(f'{j} - {inventory[str(j)]}')
                chosen_num1 = input('> ')

                if inventory[chosen_num1] != '': inventory[chosen_num1] = add_item
                else: print('Такой ячейки нет')
            
            elif chosen_num == '2':
                pass

            else:
                print('Такого варианта нет!')

    def use_items(self):
        for i in range(1,6):
            if inventory[str(i)] == '':
                pass

            else:
                print("\nВыберите предмет, который будете использовать:")

                for j in range(1,6):
                    if inventory[str(j)] == '':
                        pass

                    else:
                        print(f'{j} - {inventory[str(j)]}')

                chosen_num = input('\n> ')
                print('\nЧто вы хотите с ним сделать?')

                # Для оружия
                if any(item in inventory[chosen_num] for item in items[0]):
                    print('1 - Переложить в основную руку\n2 - Выкинуть\n3 - Ничего\n')
                    chosen_num1 = input('> ')

                    if chosen_num1 == '1':

                        if inventory['Weapon'] != '': 
                            self.switch_main_item(inventory['Weapon'],'Weapon')

                        inventory['Weapon'] = inventory[chosen_num]

                        if 'Меч' in inventory['Weapon']:
                            self.strenght += 3 + int(inventory['Weapon'][4:][:1]) * 2

                        elif 'Кинжал' in inventory['Weapon']:
                            self.strenght += 1 + int(inventory['Weapon'][7:][:1]) * 2
                            self.agility += 2 + int(inventory['Weapon'][7:][:1]) * 2

                        elif 'Лук' in inventory['Weapon']:
                            self.agility += 3 + int(inventory['Weapon'][4:][:1]) * 2

                        elif 'Копье' in inventory['Weapon']:
                            self.strenght += 2 + int(inventory['Weapon'][6:][:1]) * 2
                            self.defence += 1 + int(inventory['Weapon'][6:][:1]) * 2

                        elif 'Сковородочаки' in inventory['Weapon']:
                            self.agility += 2 + int(inventory['Weapon'][14:][:1]) * 2
                            self.defence += 2 + int(inventory['Weapon'][14:][:1]) * 2

                        inventory[chosen_num] = ''

                    elif chosen_num1 == '2':
                        inventory[chosen_num] = ''

                    elif chosen_num1 == '3':
                        pass
                
                # Для брони
                elif any(item in inventory[chosen_num] for item in items[1]):
                    print('1 - Надеть\n2 - Выкинуть\n3 - Ничего\n')
                    chosen_num1 = input('> ')

                    if chosen_num1 == '1':
                        if inventory['Armor'] != '': self.switch_main_item(inventory['Armor'],'Armor')
                        inventory['Armor'] = inventory[chosen_num]

                        if 'Латная броня' in inventory['Armor']:
                            self.defence += 5 + int(inventory['Armor'][13:][:1])

                        elif 'Кольчуга' in inventory['Armor']:
                            self.defence += 3 + int(inventory['Armor'][9:][:1])
                            self.agility += 1 + int(inventory['Armor'][9:][:1])

                        elif 'Кожаная броня' in inventory['Armor']:
                            self.defence += 2 + int(inventory['Armor'][14:][:1])
                            self.agility += 3 + int(inventory['Armor'][14:][:1])

                        inventory[chosen_num] = ''
                        
                    elif chosen_num1 == '2':
                        inventory[chosen_num] = ''

                    elif chosen_num1 == '3':
                        pass
                
                # Для расходников
                elif inventory[chosen_num] in items[2]:
                    print('1 - Выпить\n2 - Выкинуть\n3 - Ничего\n')
                    chosen_num1 = input('> ')

                    if chosen_num1 == '1':
                        if inventory[chosen_num] == 'Зелье здоровья(Маленькое)':
                            self.cur_hp += 10

                        elif inventory[chosen_num] == 'Зелье здоровья(Среднее)':
                            self.cur_hp += 25

                        elif inventory[chosen_num] == 'Зелье здоровья(Большое)':
                            self.cur_hp += 70

                        if self.cur_hp > self.max_hp:
                            self.cur_hp = self.max_hp

                        inventory[chosen_num] = ''

                    elif chosen_num1 == '2':
                        inventory[chosen_num] = ''

                    elif chosen_num1 == '3':
                        pass

                    elif inventory[chosen_num] == '':
                        print('Здесь нет предмета!')
                break
        else:
            print('\nУ вас в инвентаре ничего нет') 

    def switch_main_item(self,name,category):
        print(f'\nЧто вы хотите сделать с {name}\n1 - Вернуть в инвентарь\n2 - Выкинуть\n')
        chosen_num = input('> ')

        # Убираем характеристики предыдущего оружия
        for i in items[0]:
            if i in name:
                if 'Меч' in inventory['Weapon']:
                    self.strenght -= 3 + int(inventory['Weapon'][4:][:1]) * 2

                elif 'Кинжал' in inventory['Weapon']:
                    self.strenght -= 1 + int(inventory['Weapon'][7:][:1]) * 2
                    self.agility -= 2 + int(inventory['Weapon'][7:][:1]) * 2

                elif 'Лук' in inventory['Weapon']:
                    self.agility -= 3 + int(inventory['Weapon'][4:][:1]) * 2

                elif 'Копье' in inventory['Weapon']:
                    self.strenght -= 2 + int(inventory['Weapon'][6:][:1]) * 2
                    self.defence -= 1 + int(inventory['Weapon'][6:][:1]) * 2

                elif 'Сковородочаки' in inventory['Weapon']:
                    self.agility -= 2 + int(inventory['Weapon'][14:][:1]) * 2
                    self.defence -= 2 + int(inventory['Weapon'][14:][:1]) * 2

        for j in items[1]:
            if j in name:
                if 'Латная броня' in inventory['Armor']:
                    self.defence -= 5 + int(inventory['Armor'][13:][:1])

                elif 'Кольчуга' in inventory['Armor']:
                    self.defence -= 3 + int(inventory['Armor'][9:][:1])
                    self.agility -= 1 + int(inventory['Armor'][9:][:1])

                elif 'Кожаная броня' in inventory['Armor']:
                    self.defence -= 2 + int(inventory['Armor'][14:][:1])
                    self.agility -= 3 + int(inventory['Armor'][14:][:1])
                    
        if chosen_num == '1': self.add_in_inventory(name)

        elif chosen_num == '2': inventory[category] = ''

        else: 
            print('Такого варианта нет!')
            self.use_items()
    
    def lvl_up(self):
        while self.exp >= self.req_exp:
            self.req_exp += self.lvl
            self.lvl += 1

            self.exp = self.exp - self.req_exp
            self.stat_point += 1


    def menu(self):
        if self.cur_hp <= 0:
            print("Игра закончена")
            return self.gameover()
        
        self.change_floor()
        self.lvl_up()

        print("\nВаше действие:\n1 - Идти дальше\n2 - Просмотреть инвентарь\n3 - Использовать предмет\n4 - Посмотреть характеристики\n")
        chosen_num = input('> ')
        
        if chosen_num == '1': self.move()
        elif chosen_num == '2': self.show_inventory()
        elif chosen_num == '3': self.use_items()
        elif chosen_num == '4': self.show_stats()
        else: 
            print('Такого выбора нет!')
            self.menu()

    def move(self):
        room_list = []

        for i in range(1,3):
            chosen_room = randint(1,3)
            if chosen_room == 1: 
                self.random_hide('Боевая комната',i) 
                room_list.append('Боевая комната')

            elif chosen_room == 2: 
                self.random_hide('Комната с сокровищами',i)
                room_list.append('Комната с сокровищами')

            elif chosen_room == 3: 
                self.random_hide('Комната отдыха',i)
                room_list.append('Комната отдыха')

        print(f'\nВыберите направление, куда хотите пойти:\n1 - Налево\n2 - Направо\n')
        chosen_num = input('> ')

        if chosen_num == "1":
            if room_list[0] == 'Боевая комната': self.battle_room()

            elif room_list[0] == 'Комната с сокровищами': self.treasure_room()

            elif room_list[0] == 'Комната отдыха': self.rest_room()

        elif chosen_num == '2':
            if room_list[1] == 'Боевая комната': self.battle_room()

            elif room_list[1] == 'Комната с сокровищами': self.treasure_room()

            elif room_list[1] == 'Комната отдыха': self.rest_room()

        else:
            print('Такого выбора нет!')
            self.menu()

    def random_hide(self,name_room,num_room):
        rand_num = randint(1,2)

        if num_room == 1: 
            if rand_num == 1: print(f'\nСлева: {name_room}')
            else: print("\nСлева: ???????")

        else:
            if rand_num == 1: print(f"Справа: {name_room}")
            else: print("Справа: ???????")

    def battle_room(self):
        print("\nВы попали в боевую комнату.")
        self.show_stats()
        self.battle()
        self.room += 1
    
    def treasure_room(self):
        self.room += 1
        print('\nВы находитесь в комнате с сокровищами\nВыберите действие:\n1 - Открыть сундук\n2 - Хлопнуть дверью и выйти\n')
        chosen_num = input('> ')

        if chosen_num == '1': self.drop()

        elif chosen_num == '2': self.menu()

        else: 
            print('Такого выбора нет!')
            self.treasure_room()

    def rest_room(self):
        self.room += 1
        print(f'\nВы попали в комнату отдыха\nУ вас есть {self.stat_point} очков навыков\n\nВыберите действие:')

        if self.stat_point == 0:
            print('1 - Идти дальше\n')
            chosen_num = input('> ')

            if chosen_num == '1': self.menu()
            else: print('Такой опции нет!')

        else:
            print('1 - Идти дальше\n2 - Повысить характеристики\n')
            chosen_num = input('> ')

            if chosen_num == '1': self.menu()

            elif chosen_num == '2': self.up_stats()

            else: print('Такой опции нет!')

    def change_floor(self):
        if self.room >= 5 * self.floor:
            self.floor += 1
            print(f'\nВы перешли на {self.floor} этаж')

    def drop(self):
        rand_item = choice(items[randint(0,2)])

        # Шансы дропа для зелий
        if rand_item in items[2]:
            rand_num1 = randint(1,10)

            if 1 <= rand_num1 < 8: rand_item = items[2][0]

            elif 8 <= rand_num1 < 10: rand_item = items[2][1]

            else: rand_item = items[2][2]
            
        if rand_item in items[2]: print(f'\nВы нашли:{rand_item}')

        else: print(f'\nВы нашли:{rand_item}' + f'({self.floor})')

        print('\nВыберите действие:\n1 - Добавить в инвентарь\n2 - Выкинуть\n')
        chosen_num = input('> ')

        if rand_item in items[2]:
            if chosen_num == '1': self.add_in_inventory(rand_item)

            elif chosen_num == '2': 
                self.menu()

            else: 
                print('Такого выбора нет!')
                self.drop()
        else:
            if chosen_num == '1': self.add_in_inventory(rand_item + f'({self.floor})')

            elif chosen_num == '2': self.menu()

            else: 
                print('Такого выбора нет!')
                self.drop()

    def attack(self, mob_stats):
        crit_chance = randint(1,20)

        if self.strenght - mob_stats[4] < 0:
            print("\nВы нанесли 0 урона")

        else:
            # Критический удар
            if crit_chance == 1:
                mob_stats[0] -= (self.strenght * 2) - mob_stats[4]

                if mob_stats[0] < 0:
                    mob_stats[0] = 0

                print(f'\nВы нанесли критический удар на {(self.strenght * 2) - mob_stats[4]} урона.\nУ врага осталось {mob_stats[0]}\{mob_stats[1]} здоровья')

            else:
                mob_stats[0] -= self.strenght - mob_stats[4]

                if mob_stats[0] < 0:
                    mob_stats[0] = 0

                print(f'\nВы нанесли {self.strenght - mob_stats[4]} урона.\nУ врага осталось {mob_stats[0]}\{mob_stats[1]} здоровья')
    
    def mob_attack(self, mob_stats):
        crit_chance = randint(1,20)

        if mob_stats[2] - self.defence < 0:
            print("Вам нанесли 0 урона")

        else:
            # Критический удар
            if crit_chance == 1:
                self.cur_hp -= (mob_stats[2] * 2) - self.defence

                if self.cur_hp < 0:
                    self.cur_hp = 0

                print(f'Вам нанесли критический удар на {(mob_stats[2] * 2) - self.defence} урона.\nУ вас осталось {self.cur_hp}\{self.max_hp} здоровья')

            else:
                self.cur_hp -= mob_stats[2] - self.defence

                if self.cur_hp < 0:
                    self.cur_hp = 0

                print(f'Вам нанесли {mob_stats[2] - self.defence} урона.\nУ вас осталось {self.cur_hp}\{self.max_hp} здоровья')

    def battle(self):
        mob = Mob(self.floor,self.room)
        mob_stats = list(mob.mob_show_stats())

        while self.cur_hp > 0 and mob_stats[0] > 0:
            dodge_chance1 = False  
            print("\nВыберите действие:\n1.Нанести удар\n2.Попытаться уклониться\n3.Использовать предмет\n")
            chosen_num = input("> ")

            if chosen_num == "1":
                dodge_chance = mob_stats[3] - self.agility

                if dodge_chance <= 0:
                    self.attack(mob_stats)

                else:
                    rand_num = randint(1,20)

                    if dodge_chance > 10:
                        dodge_chance = 10

                    if dodge_chance >= rand_num:
                        dodge_chance = True

                    else:
                        dodge_chance = False

                    if dodge_chance:
                        print("Враг уклонился")

                    else:
                        self.attack(mob_stats)

            elif chosen_num == "2":
                dodge_chance1 = mob_stats[3] - self.agility

                if dodge_chance1 <= 0:
                    dodge_chance1 = 2

                rand_num = randint(1,20)

                if dodge_chance1 > 15:
                    dodge_chance1 = 15

                if dodge_chance1 >= rand_num:
                    dodge_chance1 = True

                else:
                    dodge_chance1 = False

            elif chosen_num == "3":
                self.use_items()

            else:
                print("Такого действия нет")
                self.battle()
            
            if mob_stats[0] <= 0: break

            print("\nВраг атакует!")

            if dodge_chance1:
                print("Вы уклонились")

            else:                
                dodge_chance = self.agility - mob_stats[3]

                if dodge_chance <= 0:
                    self.mob_attack(mob_stats)

                else:
                    rand_num = randint(1,20)

                    if dodge_chance > 10:
                        dodge_chance = 10

                    if dodge_chance >= rand_num:
                        dodge_chance = True

                    else:
                        dodge_chance = False

                    if dodge_chance:
                        print("Вы уклонились")

                    else:
                        self.mob_attack(mob_stats)

        if self.cur_hp <= 0:
            print("Вы погибли")

        else:
            print("Враг повержен")
            self.exp += mob_stats[5]
            self.money += mob_stats[6]
            self.drop()

    def gameover(self):
        print(f'Вы находились на {self.floor} этаже в {self.room} комнате.\nУ вас было {self.money} золота.\nВы были {self.lvl} уровня')
        print("\nВыберите действие:\n1.Начать игру заново\n2.Закончить игру\n")
        chosen_num = input("> ")

        if chosen_num == "1":
            print('Who are you?')
            self.name = input("> ")
            self.race = ''
            self.money = 0
            self.floor = 0
            self.exp = 0
            self.req_exp = 5
            self.lvl = 1
            self.stat_point = 0
            self.room = 0
            inventory = {'Weapon':'','Armor':''}
            for i in range(1,6): inventory[str(i)] = ''
            self.char_stats()
            self.show_stats()
            return False

        elif chosen_num == "2":
            return True

        else:
            print("Такого варианта нет!")