# 1. Определение множеств
U = {'к', 'о', 'м', 'п', 'ь', 'ю', 'т', 'е', 'р'}
A = {'к', 'о', 'ю', 'т', 'е', 'р'}
B = {'к', 'о', 'м', 'т'}
C = {'о', 'м', 'п', 'е', 'р'}

# 2. Выполнение операций и вывод результатов
# Для наглядности сортируем элементы перед выводом

print("Исходные множества:")
print(f"U = {sorted(U)}")
print(f"A = {sorted(A)}")
print(f"B = {sorted(B)}")
print(f"C = {sorted(C)}")
print("\nРезультаты операций:")

# а) Пересечение А и В
result_a = A & B
print(f"а) А ∩ B = {sorted(result_a)}")

# б) Пересечение В и С
result_b = B & C
print(f"б) В ∩ C = {sorted(result_b)}")

# в) Пересечение А и С
result_v = A & C
print(f"в) А ∩ C = {sorted(result_v)}")

# г) Объединение А и В
result_g = A | B
print(f"г) А ∪ B = {sorted(result_g)}")

# д) Разность А и С (элементы, которые есть в А, но нет в С)
result_d = A - C
print(f"д) А \\ C = {sorted(result_d)}")