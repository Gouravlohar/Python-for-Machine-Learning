n = 5
for i in range(n):
    for j in range(n):
        if i in [0, n - 1] or j in [0, n - 1]:
            print("*", end="")
        else:
            print(" ", end="")
    print()