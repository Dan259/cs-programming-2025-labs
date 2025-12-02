while True:
    otvet = []
    a = input('Введите 5 натуральных чисел через пробел:').split()
    print(a)
    if len(a) == 5:
        for i in range(len(a)):
            if not(a[i].replace('-','').isdigit()):
                print("Введено не число")
                break
        else:
            a = sorted(list(map(int,a)))
            if a[0] > 0:
                for x in range(5):
                    for y in range(x,5):
                        if x < y and f'({a[x]}, {a[y]})' not in otvet and a[x] != a[y]:
                            otvet.append(f'({a[x]}, {a[y]})')
            else:
                print('Введено не натуральное число')
            print(otvet)
    else:
        print('Нужно ввести 5 чисел')
