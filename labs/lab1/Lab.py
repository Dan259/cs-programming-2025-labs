def num1():
    a1 = 231
    b1 = 24.2
    c1 = 'fdas'
    d1 = True

def num2():
    a2 = 'Danil'
    b2 = 17
    print(a2,b2)

def num3():
    a3 = 342
    b3 = 56.2
    c3 = '43'
    d3 = float(a3) + b3 + float(c3)
    print(d3)

def num4():
    a4 = 3
    b4 = 8
    print(((a4 + (4 * b4)) * (a4 - (3 * b4))) + (a4**2))

def num5():
    print(int(input('')) * int(input('')))

def num6():
    print('*   *   *')
    print(' * * * *')
    print('  *  * ')

def num7():
    a7 = 5
    b7 = 3
    print(a7 + b7, a7 - b7, a7 * b7, a7 / b7, a7 ** b7, a7 // b7, a7 % b7)
    print(a7 > b7, a7 < b7, a7 <= b7, a7 >= b7, a7 == b7, a7 != b7)

def num8():
    a8 = 'Данил'
    b8 = '17'
    print(f'Меня зовут {a8} , мне {b8} лет.')

def num9():
    a9 = 'Съешь ещё '
    b9 = 'этих мягких '
    c9 = 'французких булок, '
    d9 = 'да выпей '
    e9 = 'чаю.'
    print(a9 + b9 + c9 + d9 + e9)

def num10():
    print('Нет! Да! ' * 4)

def num11():
    e11 = int(input(''))
    a11, b11, c11 = e11.split(',')
    d11 = (a11 + c11) // b11
    print('Результат вычисления: ', d11)

def num12():
    a12 = input()
    print(a12[:4])
    print(a12[8:10])
    print(a12[4:8])
    print(a12[::-1])
    
num11