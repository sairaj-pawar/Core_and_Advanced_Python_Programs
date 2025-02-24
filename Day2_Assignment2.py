##Assignment 2 - Declare two variables and print that which variable is largest using ternary operators
# Declare two variables with user input
a = int(input("Enter the first number: "))  # Taking the first number as input
b = int(input("Enter the second number: "))  # Taking the second number as input

# Use ternary operator to find the largest number
largest = a if a > b else b  # If a is greater than b, assign a to largest; otherwise, assign b

# Print the largest number
print("The largest number is:", largest)  # Display the largest number

'''Example Outputs:

# Example 1:
# Enter the first number: 10
# Enter the second number: 25
# The largest number is: 25

# Example 2:
# Enter the first number: 50
# Enter the second number: 30
# The largest number is: 50'''
