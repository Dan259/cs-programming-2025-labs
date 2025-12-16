a = input('Введите число и количество лет:').split()
b = 0
income = 0
income_all = 0
for i in range(int(a[1])):
    a1 = float(a[0])
    while b <= 4.7 and a1 > 9999:
        a1 -= 10000
        b += 0.3
        b = round(b,1)
    if i+1 <= 3: b += 3
    elif 4 <= i+1 <= 6: b += 5
    else: b += 2
    income += float(a[0]) * (b / 100)
    income = round(income,2)
    income_all += income
    a[0] = float(a[0]) + income
    print(a[0],b,income,income_all)
    b = 0
    income = 0
print(income_all)