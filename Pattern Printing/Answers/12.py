n = 5

# Print the upside-down pyramid
for i in range(n, 0, -1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print("")

# Print the normal pyramid
for i in range(2, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print("")