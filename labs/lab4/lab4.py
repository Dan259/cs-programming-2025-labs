def num1():
    a = int(input('Введите температуру:'))
    if a < 20:
        print('Кондиционер включен')
    else:
        print('Кондиционер выключен')

def num2():
    a = int(input("Введите месяц:"))
    if a > 0 and a < 3 or a == 12:
        print('Winter')
    elif a > 2 and a < 6:
        print('Spring')
    elif a > 5 and a < 9:
        print('Summer')
    elif a > 8 and a < 12:
        print('Autumn')

def num3():
    a = input('Введите возраст:')
    b = 0
    c = False
    d = []
    for i in range(1,100):
        d.append(str(i))
    
    if a in d:
        c = True

    if c == True:
        a = int(a)
        if a > 1 and a < 23:
            if a == 2:
                b = 21
                print(b)
            else:
                b = 21 + ((a-2) * 4)
                print(b)
        else:
            print('Error, age cannot be smaller than 1 and bigger than 22')
    else:
        print('Error, incorrect type of input')

def num4():
    a = input('Enter number:')
    b = 0
    for i in range(len(a)):
        b += int(a[i])
    if int(a[len(a)-1]) % 2 == 0 and b % 3 == 0:
        print('Число кратно 6')
    else:
        print('Число некратно 6')

def num5():
    a = input('Enter password:')
    b1 = ['1','2','3','4','5','6','7','8','9','0']
    b2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    b3 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    b4 = ['`','~','!','@','#','№','$','%','^','&','*','(',')','-','=','+','[',']','{','}','/','<','>',':',';']
    c1 = False
    c2 = False
    c3 = False
    c4 = False
    for i in range(len(a)):
        if a[i] in b1:
            c1 = True
        if a[i] in b2:
            c2 = True
        if a[i] in b3:
            c3 = True
        if a[i] in b4:
            c4 = True

    if c1 == False:
        print('Пароль ненадёжный, отсутствуют цифры')
    if c2 == False:
        print('Пароль ненадёжный, отсутствуют заглавные буквы')
    if c3 == False:
        print('Пароль ненадёжный, отсутствуют строчные буквы')
    if c4 == False:
        print('Пароль ненадёжный, отсутствуют специальные символы')
    if c1 == True and c2 == True and c3 == True and c4 == True:
        print('Пароль надёжный')

def num6():
    a = int(input('Enter year:'))
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print(a,'- високосный год')
    else:
        print(a,'- не високосный год')

def num7():
    a = input('Введите 3 числа через запятую:')
    b = []
    c,d,e = a.split(',')
    b.append(int(c))
    b.append(int(d))
    b.append(int(e))
    n_min = 100
    n_max = 0
    for i in range(3):
        if n_min > b[i]:
            n_min = b[i]
        if n_max < b[i]:
            n_max = b[i]
    print('Минимальное число -',n_min)
    print('Максимальное число -',n_max)

def num8():
    a = int(input('Enter sum:'))
    if a < 1000:
        print('Ваша скидка: 0%')
        print('Итоговая сумма:',a)
    elif a > 1000 and a < 5000:
        print('Ваша скидка: 5%')
        print('Итоговая сумма:',a*0.95)
    elif a > 5000 and a < 10000:
        print('Ваша скидка: 10%')
        print('Итоговая сумма:',a*0.9)
    elif a > 10000:
        print('Ваша скидка: 15%')
        print('Итоговая сумма:',a*0.85)

def num9():
    a = int(input("Введите час:"))
    if a > 0 and a < 6:
        print('Сейчас ночь')
    elif a > 5 and a < 12:
        print('Сейчас утро')
    elif a > 11 and a < 18:
        print('Сейчас день')
    elif a > 17 and a < 24:
        print('Сейчас вечер')

def num10():
    a = input('Введите число:')
    b = True
    if a.isdigit():
        a = int(a)
        for i in range(2,a):
            if a < 1 or a % i == 0:
                b = False
        if b == True:
            print('Число простое')
        else:
            print('Число не простое')
    else:
        print('Введено не число')
    

num10()
