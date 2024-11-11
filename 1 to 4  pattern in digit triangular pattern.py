'''
*
* *
* * *
* * * *
'''
# Loop through rows from 1 to 4
for i in range(1, 5):
    # Loop through columns in each row
    for j in range(1, i + 1):
        # Print an asterisk with a space at the end
        print("*", end=" ")
    # Move to the next line after each row is printed
    print("")
print("----------------------------------------------------------")
'''
1
1 2 
1 2 3
1 2 3 4
'''
# Loop through rows from 1 to 4
for i in range(1, 5):
    # Loop through columns in each row
    for j in range(1, i + 1):
        # Print the current column number in the row, with a space at the end
        print(j, end=" ")
    # Move to the next line after each row is printed
    print()
print("----------------------------------------------------------")  
'''
1
2 2 
3 3 3
4 4 4 4
'''
# Loop to control the number of rows (from 1 to 4)
for i in range(1, 5):
    # Inner loop to print the row number 'i' multiple times in each row
    for j in range(1, i + 1):
        # Print the current row number with a space, staying on the same line
        print(i, end=" ")
    # Move to the next line after each row is printed
    print()