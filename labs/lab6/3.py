a = input("Введите начало  и конец:").split()
a = list(map(int,a))
b = []
c = []

#Нахождение всех сложных чисел
for i in range(a[0],a[1]+1):
    for j in range(2,a[1]+1):
        if i % j == 0 and i != j:
            b.append(i)
            break

#Выбор простых чисел
for i in range(a[0],a[1]+1):
    if i not in b:
        c.append(i)

#Вывод и обработка ошибки
if c == []:
    print('Error!')
else:
    print(c)