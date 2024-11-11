# Function to calculate factorial
def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result

# Taking user input
number = int(input("Enter a number to get its factorial: "))
print(f"The factorial of {number} is {factorial(number)}.")
