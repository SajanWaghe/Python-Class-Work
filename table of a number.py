# Function to print multiplication table
def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Taking user input
number = int(input("Enter a number to get its multiplication table: "))
multiplication_table(number)
