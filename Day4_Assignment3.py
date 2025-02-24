#Assignment 3 - Python Program to Check if a Number is Positive, Negative, or Zero

# Take input from the user
num = float(input("Enter a number: "))  # Taking input as a float to handle decimals

# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is Positive.")
elif num < 0:
    print("The number is Negative.")
else:
    print("The number is Zero.")

'''Output'''

'''
Example 1:
Enter a number: 10
The number is Positive.

Example 2:
Enter a number: -5
The number is Negative.

Example 3:
Enter a number: 0
The number is Zero.

Example 4:
Enter a number: 3.5
The number is Positive.
'''
