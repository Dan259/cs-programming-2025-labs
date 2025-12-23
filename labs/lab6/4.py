a = input('').split()
b = []
c = []
e = False
while True:
    #Проверка разрерности матриц
    if int(a[0]) <= 2 or int(a[1]) <= 2:
        print('Error! Размерность матрицы слишком маленькая')
        break

    #Введение матриц
    print('Введите первую матрицу:')
    for i in range(int(a[0])):
        b.append(list(map(int,input(f'Введите {i+1} строку:').split())))
    print("Введите вторую матрицу:")
    for i in range(int(a[0])):
        c.append(list(map(int,input(f'Введите {i+1} строку:').split())))

    #Обработка ошибок
    for i in range(int(a[0])):
        if len(b[i]) != int(a[1]):
            print('Error! Количество символов в строке не соответствует размерности')
            e = True
        if len(c[i]) != int(a[1]):
            print('Error! Количество символов в строке не соответствует размерности')
            e = True
    if e == True:
        break

    #Сложение и вывод
    for i in range(int(a[0])):
        res = []
        for j in range(int(a[1])):
            res.append(b[i][j] + c[i][j])
        print(res)
    break