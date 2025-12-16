a = input("Введите начало  и конец:").split()
a = list(map(int,a))
b = []
c = []
for i in range(a[0],a[1]+1):
    for j in range(2,a[1]+1):
        if i % j == 0 and i != j:
            b.append(i)
            break
for i in range(a[0],a[1]+1):
    if i not in b:
        c.append(i)
if c == []:
    print('Error!')
else:
    print(c)