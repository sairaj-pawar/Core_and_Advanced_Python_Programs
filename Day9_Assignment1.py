'''Assignment 1 - Write a Python program to Count all letters, digits, and special symbols from the given 

string Input = “P@#yn26at^&i5ve”

 Output: Chars = 8 Digits = 2 Symbol = 3'''


# Define the input string
input_str = "P@#yn26at^&i5ve"

# Initialize counters
char_count = 0  # For letters (alphabets)
digit_count = 0  # For digits (numbers)
symbol_count = 0  # For special characters

# Iterate through each character in the string
for char in input_str:
    if char.isalpha():  # Check if the character is a letter
        char_count += 1
    elif char.isdigit():  # Check if the character is a digit
        digit_count += 1
    else:  # If it's neither a letter nor a digit, it's a special symbol
        symbol_count += 1

# Print the counts
print(f"Chars = {char_count} Digits = {digit_count} Symbol = {symbol_count}" )


'''
   Output :

'''
