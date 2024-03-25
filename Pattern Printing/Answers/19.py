rows = 5

# Upper half of the diamond
for i in range(1, rows * 2):
    if i <= rows:
        for j in range(i):
            print("*", end="")
        for k in range((rows - i) * 2):
            print(" ", end="")
        for l in range(i):
            print("*", end="")
    else:
        for j in range(rows * 2 - i):
            print("*", end="")
        for k in range((i - rows) * 2):
            print(" ", end="")
        for l in range(rows * 2 - i):
            print("*", end="")
    print()
