# Prompt user to enter the distance in kilometers and convert it to an integer
kilometers = int(input("Enter distance in kilometers: "))

# Convert the distance from kilometers to miles (1 kilometer = 0.621371 miles)
miles = kilometers * 0.621371

# Display the converted distance in miles
print("Distance in miles:", miles)