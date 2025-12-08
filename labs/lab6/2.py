a = input('Введите сумму и количество лет:').split()
b = 0
income = 0
for i in range(int(a[1])):
    a1 = int(a[0])
    while b <= 4.7 and a1 >= 9999:
        a1 -= 10000
        b += 0.3
        b = round(b,1)
    if i <= 3: b += 3
    elif 4 <= i <= 6: b += 5
    else: b += 2
    income += int(a[0]) * (b / 100)
    a[0] = int(a[0]) + income
    print(b,a[0],income)
    b = 0
print(income)
