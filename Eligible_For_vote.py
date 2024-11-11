# Prompt user to enter their birth year and convert it to an integer
birth_year = int(input("Enter your birth year: "))

# Prompt user to enter the current year and convert it to an integer
current_year = int(input("Enter the current year: "))

# Calculate the user's age based on the birth year and current year
age = current_year - birth_year

# Display the user's calculated age
print("Your age is:", age)

# Determine and display voting eligibility based on the age
if (age >= 18):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")