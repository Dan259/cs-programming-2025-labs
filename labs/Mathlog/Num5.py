a = int(input("Введите кол-во взрослых:"))
b = int(input("Введите кол-во взрослых, которым нужно проверить здоровье:"))
c = int(input("Введите кол-во детей:"))
d = int(input("Введите кол-во детей, которым нужно проверить здоровье:"))
from math import factorial
res1 = factorial(a) / (factorial(a - b) * factorial(b))
res2 = factorial(c) / (factorial(c - d) * factorial(d))
res = res1 * res2
print(f'Всего есть {res} способов')