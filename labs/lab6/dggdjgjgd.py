a = input('').split()
b = []
c = []
res = []
print('Введите первую матрицу:')
for i in range(int(a[0])):
    b.append(list(map(int,input(f'Введите {i+1} строку:').split())))
print("Введите вторую матрицу:")
for i in range(int(a[0])):
    c.append(list(map(int,input(f'Введите {i+1} строку:').split())))
for i in range(int(a[0])):
    for j in range(int(a[1])):
        res.append(b[i][j] + c[i][j])
    print(res)
    res.clear()