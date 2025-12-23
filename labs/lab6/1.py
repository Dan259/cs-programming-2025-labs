a = input('Введите время:').split()
a.append(a[0][len(a[0])-1])
a[0] = a[0][:len(a[0])-1]
ans = 0

#Перевод для минут
if a[2] == 'm':
    if a[1] == 'h':
        ans = float(a[0]) / 60
    elif a[1] == 's':
        ans = float(a[0]) * 60

#Перевод для секунд
elif a[2] == 's':
    if a[1] == 'm':
        ans = float(a[0]) / 60
    elif a[1] == 'h':
        ans = float(a[0]) / 3600

#Перевод для часов
elif a[2] == 'h':
    if a[1] == 'm':
        ans = float(a[0]) * 60
    elif a[1] == 's':
        ans = float(a[0]) * 3600
print(ans,a[1])