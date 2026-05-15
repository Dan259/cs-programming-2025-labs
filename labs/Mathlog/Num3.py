from math import *
a = int(input("Введите кол-во выпечки на выбор:"))
b = int(input("Введите кол-во выпечки, которую необходимо купить:"))
res = factorial(b + a - 1) / (factorial(b) * factorial(a - 1))
print(f'Всего существует {res} способов выбора выпечки')