#Assignment 1 - Python program to check leap year  or not. 
# Take input from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year using conditions
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year, "is a Leap Year")
else:
    print(year, "is NOT a Leap Year")

'''Output'''

'''
Example 1:
Enter a year: 2024
2024 is a Leap Year

Example 2:
Enter a year: 2023
2023 is NOT a Leap Year

Example 3:
Enter a year: 2000
2000 is a Leap Year

Example 4:
Enter a year: 1900
1900 is NOT a Leap Year
'''
