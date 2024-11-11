# Initialize the total variable to 0
total = 0

# Loop through numbers 1 to 10
for i in range(1, 11):
    # Store the current total before adding the current number
    t = total
    # Add the current number to the total
    total += i
    # Print the equation for the current step
    print(i, "+", t, "=", total)

# Print the final total after the loop completes
print("The total is:", total)