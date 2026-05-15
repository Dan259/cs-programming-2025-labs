from math import factorial
a = int(input("Введите кол-во участников кворума:")) - 1
b = int(input("Введите кол-во минимальных участников кворума:")) - 1
res = factorial(a) / (factorial(a - b) * factorial(b))
print(f'Всего есть {12 * res} способов')