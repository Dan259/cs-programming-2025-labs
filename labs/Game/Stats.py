from random import *

items = [['Меч','Кинжал','Лук','Копье','Сковородочаки'],['Латная броня','Кольчуга','Кожаная броня'],['Зелье здоровья(Маленькое)','Зелье здоровья(Среднее)','Зелье здоровья(Большое)']]
inventory = {'Weapon':'','Armor':''}
for i in range(1,6): inventory[str(i)] = ''


class Character:
    def __init__(self):
        print('Who are you?')
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

    def char_stats(self):
        print("Выберите расу:")
        print("1 - Человек")
        print("2 - Эльф")
        print("3 - Дворф")
        self.race = input("> ")
        # Создание человека
        if self.race == "1":
            self.max_hp = randint(90,110)
            self.strenght = randint(4,8)
            self.agility = randint(5,10)
            self.defence = randint(3,5)
            self.height = randint(150,200)
            self.weight = randint(60,90)
            if self.weight < 70 and self.height < 160:
                self.strenght -= 1
                self.agility += 1
            elif self.weight > 80 and self.height > 190:
                self.strenght += 1
                self.agility -= 1
            print("Ваш персонаж создан!")
            
        # Создание эльфа
        elif self.race == "2":
            self.max_hp = randint(70,90)
            self.strenght = randint(4,8)
            self.agility = randint(8,14)
            self.defence = randint(3,5)
            self.height = randint(175,210)
            self.weight = randint(40,70)
            if self.weight < 50 and self.height < 185:
                self.strenght -= 1
                self.agility += 2
            elif self.weight > 60 and self.height > 200:
                self.strenght += 1
                self.agility -= 1
            print("Ваш персонаж создан!")

        # Создание дворфа
        elif self.race == "3":
            self.max_hp = randint(100,130)
            self.strenght = randint(5,10)
            self.agility = randint(3,6)
            self.defence = randint(6,10)
            self.height = randint(100,130)
            self.weight = randint(70,100)
            if self.weight < 80 and self.height < 110:
                self.strenght -= 1
                self.agility += 1
            elif self.weight > 90 and self.height > 120:
                self.strenght += 2
                self.agility -= 1
            print("Ваш персонаж создан!")
        else:
            print("Такой расы нет!")
            self.char_stats()
        self.cur_hp = self.max_hp
        return self.max_hp, self.strenght, self.agility, self.defence, self.height, self.weight
    
    def show_stats(self):
        print('ВАШ ПЕРСОНАЖ:')
        print('---------')
        print(f'Name:{self.name}')
        print('---------')
        print(f'LVL:{self.lvl}')
        print(f'EXP:{self.exp}\{self.req_exp}')
        print('---------')
        print(f'HP:{self.cur_hp}\{self.max_hp}')
        print(f'STR:{self.strenght}')
        print(f'AGI:{self.agility}')
        print(f'DEF:{self.defence}') 
        print('---------')

    def up_stats(self):
        print("Выберите характеристику:\n1 - +2 к HP\n2 - +1 к атаке\n3 - +1 к ловкости\n4 - +1 к броне")
        num_up = input('> ')
        if num_up == "1":
            self.max_hp += 2
        elif num_up == "2":
            self.strenght += 1
        elif num_up == "3":
            self.agility += 1
        elif num_up == "4":
            self.defence += 1
        else:
            print("Такой опции нет")
    
    def show_inventory(self):
        global inventory
        print(f'Weapon - {inventory['Weapon']}\nArmor - {inventory['Armor']}')
        for i in range(1,6):
            print(f'{i} - {inventory[str(i)]}')
        print(f'Money - {self.money}')

    def add_in_inventory(self,add_item):
        global inventory
        for i in range(1,6):
            if inventory[str(i)] == '':
                inventory[str(i)] = add_item
                break
        else:
            print('Ваш инвентарь заполнен.\nЧто вы будете делать?\n1 - Выбросить что-то из инвентаря\n2 - Не подбирать вещь')
            chosen_num = input('> ')
            if chosen_num == '1':
                print('Выберите вещь, которую выкините:')
                for j in range(1,6):
                    print(f'{j} - {inventory[str(j)]}')
                chosen_num1 = input('> ')
                if inventory[chosen_num1] != '': inventory[chosen_num1] = add_item
                else: print('Такой ячейки нет')



    def use_items(self):
        for i in range(1,6):
            if inventory[str(i)] == '':
                pass
            else:
                print("Выберите предмет, который будете использовать:")
                for j in range(1,6):
                    if inventory[str(j)] == '':
                        pass
                    else:
                        print(f'{j} - {inventory[str(j)]}')
                choosen_num = input('> ')
                print('Что вы хотите с ним сделать?')

                # Для оружия
                if any(item in inventory[choosen_num] for item in items[0]):
                    print('1 - Переложить  в основную руку\n2 - Выкинуть\n3 - Ничего')
                    choosen_num1 = input('> ')
                    if choosen_num1 == '1':
                        if inventory['Weapon'] != '': self.switch_main_item(inventory['Weapon'],'Weapon')
                        inventory['Weapon'] = inventory[choosen_num]
                        if 'Меч' in inventory['Weapon']:
                            self.strenght += 3 + int(inventory['Weapon'][4:][:1])
                        elif 'Кинжал' in inventory['Weapon']:
                            self.strenght += 1 + int(inventory['Weapon'][7:][:1])
                            self.agility += 2 + int(inventory['Weapon'][7:][:1])
                        elif 'Лук' in inventory['Weapon']:
                            self.agility += 3 + int(inventory['Weapon'][4:][:1])
                        elif 'Копье' in inventory['Weapon']:
                            self.strenght += 2 + int(inventory['Weapon'][6:][:1])
                            self.defence += 1 + int(inventory['Weapon'][6:][:1])
                        elif 'Сковородочаки' in inventory['Weapon']:
                            self.agility += 2 + int(inventory['Weapon'][14:][:1])
                            self.defence += 2 + int(inventory['Weapon'][14:][:1])
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '2':
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '3':
                        pass
                
                # Для брони
                elif any(item in inventory[choosen_num] for item in items[1]):
                    print('1 - Надеть\n2 - Выкинуть\n3 - Ничего')
                    choosen_num1 = input('> ')
                    if choosen_num1 == '1':
                        if inventory['Armor'] != '': self.switch_main_item(inventory['Armor'],'Armor')
                        inventory['Armor'] = inventory[choosen_num]
                        if 'Латная броня' in inventory['Armor']:
                            self.defence += 5 + int(inventory['Armor'][13:][:1])
                        elif 'Кольчуга' in inventory['Armor']:
                            self.defence += 3 + int(inventory['Armor'][9:][:1])
                            self.agility += 1 + int(inventory['Armor'][9:][:1])
                        elif 'Кожаная броня' in inventory['Armor']:
                            self.defence += 2 + int(inventory['Armor'][15:][:1])
                            self.agility += 3 + int(inventory['Armor'][15:][:1])
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '2':
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '3':
                        pass
                
                # Для расходников
                elif inventory[choosen_num] in items[2]:
                    print('1 - Выпить\n2 - Выкинуть\n3 - Ничего')
                    choosen_num1 = input('> ')
                    if choosen_num1 == '1':
                        if inventory[choosen_num] == 'Зелье здоровья(Маленькое)':
                            self.cur_hp += 10
                        elif inventory[choosen_num] == 'Зелье здоровья(Среднее)':
                            self.cur_hp += 25
                        elif inventory[choosen_num] == 'Зелье здоровья(Большое)':
                            self.cur_hp += 70
                        if self.cur_hp > self.max_hp:
                            self.cur_hp = self.max_hp
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '2':
                        inventory[choosen_num] = ''
                    elif choosen_num1 == '3':
                        pass

                    elif inventory[choosen_num] == '':
                        print('Здесь нет предмета!')
                break
        else:
            print('У вас в инвентаре ничего нет') 

    def switch_main_item(self,name,category):
        print(f'Что вы хотите сделать с {name}\n1 - Вернуть в инвентарь\n2 - Выкинуть')
        chosen_num = input('> ')
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
            self.up_stats()


    def menu(self):
        print("\nВаше действие:\n1 - Идти дальше\n2 - Просмотреть инвентарь\n3 - Использовать предмет\n4 - Посмотреть характеристики")
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
        print(f'Выберите направление, куда хотите пойти:\n1 - Налево\n2 - Направо')
        chosen_num = input('> ')
        if chosen_num == "1":
            if room_list[0] == 'Боевая комната':
                self.battle_room()
            elif room_list[0] == 'Комната с сокровищами':
                self.treasure_room()
            elif room_list[0] == 'Комната отдыха':
                self.rest_room()
        elif chosen_num == '2':
            if room_list[1] == 'Боевая комната':
                self.battle_room()
            elif room_list[1] == 'Комната с сокровищами':
                self.treasure_room()
            elif room_list[1] == 'Комната отдыха':
                self.rest_room()
        else:
            print('Такого выбора нет!')
            self.menu()

    def random_hide(self,name_room,num_room):
        rand_num = randint(1,2)
        if num_room == 1: 
            if rand_num == 1: print(f'Слева: {name_room}')
            else: print("Слева: ???????")
        else:
            if rand_num == 1: print(f"Справа: {name_room}")
            else: print("Справа: ???????")

    def battle_room(self):
        pass
        # Мобы и боёвка
    
    def treasure_room(self):
        print('Вы находитесь в комнате с сокровищами\nВыберите действие:\n1 - Открыть сундук\n2 - Хлопнуть дверью и выйти')
        chosen_num = input('> ')
        if chosen_num == '1':
            rand_num = randint(1,3)
            if rand_num == 1 or rand_num == 2: rand_num = 1
            else: rand_num = 2
            for i in range(rand_num):
                rand_item = choice(items[randint(0,2)])
                if rand_item in items[2]: print(f'Вы нашли:{rand_item}')
                else: print(f'Вы нашли:{rand_item}' + f'({self.floor})')
                print('Выберите действие:\n1 - Добавить в инвентарь\n2 - Выкинуть')
                chosen_num = input('> ')
                if rand_item in items[2]:
                    if chosen_num == '1': self.add_in_inventory(rand_item)
                    elif chosen_num == '2': 
                        self.menu()
                        break
                    else: 
                        print('Такого выбора нет!')
                        self.treasure_room()
                else:
                    if chosen_num == '1': self.add_in_inventory(rand_item + f'({self.floor})')
                    elif chosen_num == '2': self.menu()
                    else: 
                        print('Такого выбора нет!')
                        self.treasure_room()
        elif chosen_num == '2': self.menu()
        else: 
            print('Такого выбора нет!')
            self.treasure_room()

    def rest_room(self):
        pass
        # Меню с лвлапом