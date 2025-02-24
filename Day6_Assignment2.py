# Assignment  - Write a python program to check whether a number is palindrome or not?
# Take input from the user
num = int(input("Enter a number: "))

# Store the original number to compare later
original_num = num  
rev = 0  # Variable to store the reversed number

# Reverse the number using a while loop
while num > 0:
    digit = num % 10  # Extract the last digit
    rev = (rev * 10) + digit  # Append the digit to rev
    num = num // 10  # Remove the last digit

# Check if the original number and reversed number are the same
if original_num == rev:
    print("The number is a Palindrome.")
else:
    print("The number is NOT a Palindrome.")

''' 
Output:

Example 1:
Enter a number: 121
The number is a Palindrome.

Example 2:
Enter a number: 123
The number is NOT a Palindrome.
'''
