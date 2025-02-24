# Take input from the user
num = int(input("Enter a number: "))

# Initialize factorial variable
fact = 1  
i = num  # Set i to the given number

# Calculate factorial using while loop
while i > 0:
    fact *= i  # Multiply fact by i
    i -= 1  # Decrease i by 1

# Print the factorial result
print("Factorial of", num, "is:", fact)

''' 
Output:

Example 1:
Enter a number: 5
Factorial of 5 is: 120

Example 2:
Enter a number: 4
Factorial of 4 is: 24
'''
