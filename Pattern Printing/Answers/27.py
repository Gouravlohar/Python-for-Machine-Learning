n = 4
for i in range(n):
    for j in range(1, n - i + 1):
        print(j + i * n, end=" ")
    for j in range(n - i, 0, -1):
        print(j + (n - 1) * n, end=" ")
    print()