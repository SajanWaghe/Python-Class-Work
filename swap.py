# Prompt user to enter the first number and convert it to an integer
n1 = int(input("Enter the 1st number: "))

# Prompt user to enter the second number and convert it to an integer
n2 = int(input("Enter the 2nd number: "))

# Store the value of n1 in a temporary variable 'w' to facilitate the swap
w = n1

# Assign the value of n2 to n1
n1 = n2

# Assign the original value of n1 (stored in w) to n2
n2 = w

# Display the swapped values
print("After swapping, the 1st number is:", n1)
print("After swapping, the 2nd number is:", n2)