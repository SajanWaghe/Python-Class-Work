# Function to find the maximum of two numbers
def find_max(num1, num2):
    return num1 if num1 > num2 else num2

# Taking user input
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
print(f"The maximum of {number1} and {number2} is {find_max(number1, number2)}.")
