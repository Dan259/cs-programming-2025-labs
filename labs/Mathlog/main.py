count1 = 0
count2 = 0
count3 = 0
while True:
    a = input('Введите 5 пар чисел:').split()
    for i in a:
        i = [int(x) for x in i.split(',')]
        if i[0] < i[1]:
            count1 += 1
        if i[0] > i[1]:
            count2 += 1
        if i[0] == i[1]:
            count3 += 1
    for i in 1,2,3:
        if eval(f'count{i}') == 5:
            print(f'P{i} для любой')
        else:
            print(f'P{i} не для любой')
        if eval(f'count{i}') != 0:
            print(f'P{i} существует {eval(f'count{i}')}')
        else:
            print(f'P{i} не существует')