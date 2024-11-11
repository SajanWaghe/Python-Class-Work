# Function to check voting eligibility
def can_vote(age):
    return age >= 18

# Taking user input
age = int(input("Enter your age: "))
if can_vote(age):
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
