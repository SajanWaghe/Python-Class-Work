# List of fruits
l = ["Apple", "Banana", "Cherry", "Pear", "Plum"]

# The element to search for in the list
s = "Plum"

# Flag to indicate whether the element is found
found = False

# Iterate through the list to check if the element exists
for i in l:
    if i == s:
        # If the element is found, print a message and set the flag to True
        print("Element found")
        found = True
        break  # Exit the loop once the element is found

# If the element is not found, print a message
if not found:
    print("Element is not in the list")