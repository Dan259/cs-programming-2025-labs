from math import factorial
a = int(input("Введите кол-во участников кворума:"))
b = int(input("Введите кол-во минимальных участников кворума:"))
res = factorial(a) / (factorial(a - b) * factorial(b))
print(f'Всего есть {res} способов')