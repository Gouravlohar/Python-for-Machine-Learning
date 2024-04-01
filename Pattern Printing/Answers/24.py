n = 5

# Upper Half Part
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if i == 1 or j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(1, (n - i) * 2 + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        if i == 1 or j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower Half Part
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if i == 1 or j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    for j in range(1, (n - i) * 2 + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        if i == 1 or j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
