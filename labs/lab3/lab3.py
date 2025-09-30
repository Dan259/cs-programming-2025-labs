def num1():
    a = input("Enter name:")
    b = int(input('Enter age:'))
    for i in range(0,10):
        print(f'My name {a} and Im {b} yers old')

def num2():
    a = int(input('Enter number between 1 and 9:'))
    for i in range(1,11):
        print(a * i)

def num3():
    for i in range(1,101,3):
        print(i)

def num4():
    a = int(input('Enter number:'))
    b = 1
    for i in range(1,a+1):
        b = b * i
    print(b)

def num5():
    a = 20
    while a > -1:
        print(a)
        a -= 1

def num6():
    a = int(input('Enter number:'))
    c = [0,1]
    c1 = 0
    b = 1
    b_old = 0
    while a > b:
        b += b_old
        c.append(b)
        c1 += 1
        b_old = c[c1]
    print(c[c1])

def num7():
    a = 'hello'
    b = ''
    for i in range(1,6):
        b += a[i-1] + str(i)
    print(b)

def num8():
    while True:
        a = input('Enter 2 numbers:')
        b,c = a.split(' ')
        d = int(b) + int(c)
        print(d)
        
