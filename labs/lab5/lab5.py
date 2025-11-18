from random import randint

def num1():
    a = [1,2,3,4,5,6,7,8,9,10]
    for i in range(0,10):
        if a[i] == 3:
            a[i] = 30
    print(a)

def num2():
    a = [2,3,4,5,6]
    for i in range(5):
        a[i] = a[i]**2
    print(a)

def num3():
    a = [3,6,123,451,1,34,76,2,34]
    print(max(a) / len(a))

def num4():
    a = ('2','3','1','23','12','67')
    b = True
    for i in range(len(a)):
        if not(a[i].isdigit()):
            b = False
    if b:
        a = list(map(int,a))
        a = tuple(sorted(a))
        print(a)
    else:
        print("В кортеже есть слово")
    
def num5():
    a = {'apple' : 21,'milk' : 100,'bread' : 35,'orange' : 45}
    b = 0
    c = 100000
    e = ''
    d = ''
    for i,j in a.items():
        if j > b:
            b = j
            d = i
        if j < c:
            c = j
            e = i
    print(f"Max {d}, min {e}")

def num6():
    a = ['12','a','r']
    b = {}
    for i in range(len(a)):
        b[a[i]] = a[i]
    print(b)

def num7():
    a = {'Молоко':'Milk','Хлеб':'Bread','Яблоко':'Apple'}
    b = input('Введите слово на русском: ')
    print(a[b])

def num8():
    a = input('Введите слово:')
    b = ['Камень','Ножницы','Бумага','Ящерица','Спок']
    c = randint(0,4)
    print('Компьютер выбрал',b[c])
    if a == 'Камень' and b[c] == 'Ножницы': print('Игрок победил')
    elif a == 'Камень' and b[c] == 'Ящерица': print('Игрок победил')
    elif a == 'Камень' and b[c] == 'Спок': print('Компьютер победил')
    elif a == 'Камень' and b[c] == 'Бумага': print('Компьютер победил')
    elif a == 'Ножницы' and b[c] == 'Бумага': print('Игрок победил')
    elif a == 'Ножницы' and b[c] == 'Ящерица': print('Игрок победил')
    elif a == 'Ножницы' and b[c] == 'Спок': print('Компьютер победил')
    elif a == 'Ножницы' and b[c] == 'Камень': print('Компьютер победил')
    elif a == 'Бумага' and b[c] == 'Камень': print('Игрок победил')
    elif a == 'Бумага' and b[c] == 'Ножницы': print('Компьютер победил')
    elif a == 'Бумага' and b[c] == 'Ящерица': print('Компьютер победил')
    elif a == 'Бумага' and b[c] == 'Спок': print('Игрок победил')
    elif a == 'Ящерица' and b[c] == 'Ножницы': print('Компьютер победил')
    elif a == 'Ящерица' and b[c] == 'Камень': print('Компьютер победил')
    elif a == 'Ящерица' and b[c] == 'Бумага': print('Игрок победил')
    elif a == 'Ящерица' and b[c] == 'Спок': print('Игрок победил')
    elif a == 'Спок' and b[c] == 'Камень': print('Игрок победил')
    elif a == 'Спок' and b[c] == 'Бумага': print('Компьютер победил')
    elif a == 'Спок' and b[c] == 'Ящерица': print('Компьютер победил')
    elif a == 'Спок' and b[c] == 'Ножницы': print('Игрок победил')

num8()