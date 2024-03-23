n = 4

# Print the upper half of the diamond
for i in range(1, n+1):
    # Print leading spaces
    for j in range(n-i):
        print(" ", end="")
    # Print numbers
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print("")

# Print the lower half of the diamond
for i in range(n-1, 0, -1):
    # Print leading spaces
    for j in range(n-i):
        print(" ", end="")
    # Print numbers
    for j in range(i, 0, -1):
        print(j, end="")
    for j in range(2, i+1):
        print(j, end="")
    print("")