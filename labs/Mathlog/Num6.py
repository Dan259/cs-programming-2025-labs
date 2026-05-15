from math import factorial
a = input("Введите слово:")
a1 = ""
res = 1
for i in a:
    if i not in a1:
        a1 += i
for i in range(len(a1)):
    res *= factorial(a.count(a1[i]))
res1 = factorial(len(a)) / res
print(f'Всего {res1} машинных слов')