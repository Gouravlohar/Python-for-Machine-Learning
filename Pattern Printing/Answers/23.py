num_stars = 5
for i in range(num_stars):
  # Print leading spaces
  for j in range(num_stars - i - 1):
    print(" ", end="")
  # Print stars
  for j in range(2 * i + 1):
    print("*", end="")
  print()

# Print a single line of stars in the middle
print(" " * (num_stars // 2) + "*")
