a = input('Введите время открытия и закрытия магазина:').split()
b = input('Введите время начала и конца сиесты:').split()
c = input('Введите время посещение магазина Васей:')
if int(a[0]) > int(a[1]) or int(b[0]) > int(b[1]):
    print('Error')
else:
    if int(a[0]) <= int(c) < int(b[0]) or int(b[1]) <= int(c) < int(a[1]):
        print('Магазин открыт')
    else:
        print('Магазин закрыт')