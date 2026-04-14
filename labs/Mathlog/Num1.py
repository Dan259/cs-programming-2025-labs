A = [1, 2, 3, 4, 5, 6]

def remainder(x):
    return x % 3

n = len(A)
R = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if remainder(A[i]) == remainder(A[j]):
            R[i][j] = 1

print("Полная матрица отношения R1:")
print("   ", " ".join(str(x) for x in A))
for i in range(2):
    print(f"{A[i]} |", " ".join(str(R[i][j]) for j in range(n)))

print("\nПервая строка (элемент 1):", R[0])

print("Вторая строка (элемент 2):", R[1])