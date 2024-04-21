n = 7  # size of the matrix
for i in range(n):
    for j in range(n):
        print(max(n - i, i + 1, n - j, j + 1), end=' ')
    print()