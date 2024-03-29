n = 5
for i in range(n):
    for j in range(i + 1):
        print((i + j+1) % 2, end=" ")
    print()