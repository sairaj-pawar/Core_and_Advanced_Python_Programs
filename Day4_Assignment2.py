#Assignment 2 - Python Program to Find the Largest Among Three Numbers 

# Take three numbers as input from the user
a = int(input("Enter first number: "))  
b = int(input("Enter second number: "))  
c = int(input("Enter third number: "))  

# Check which number is the greatest using if-elif conditions
if a > b and a > c:  
    greatest = a  # If 'a' is greater than both 'b' and 'c', assign 'a' to greatest
elif b > c:  
    greatest = b  # If 'b' is greater than 'c', assign 'b' to greatest
else:  
    greatest = c  # If the above conditions fail, 'c' is the greatest

# Print the greatest number
print("The greatest number is:", greatest)  

'''Output'''

'''
Example 1:
Enter first number: 10
Enter second number: 25
Enter third number: 15
The greatest number is: 25

Example 2:
Enter first number: 50
Enter second number: 30
Enter third number: 40
The greatest number is: 50

Example 3:
Enter first number: 5
Enter second number: 5
Enter third number: 8
The greatest number is: 8
'''
