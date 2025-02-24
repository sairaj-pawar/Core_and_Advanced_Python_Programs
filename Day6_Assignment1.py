#Assignment 1 = Write a python program finding the factorial of a given number using a while loop.

# Take input from the user
num = int(input("Enter a number: "))

# Variable to store the reversed number
rev = 0  

# Reverse the number using a while loop
while num > 0:
    digit = num % 10  # Get the last digit
    rev = (rev * 10) + digit  # Append the digit to reversed number
    num = num // 10  # Remove the last digit from original number

# Print the reversed number
print("Reversed number:", rev)

''' 
Output:

Example 1:
Enter a number: 1234
Reversed number: 4321

Example 2:
Enter a number: 56789
Reversed number: 98765
'''
