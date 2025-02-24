'''Assignment 2 - Write a Python program to remove duplicate characters of a given string. 

Input = “String and String Function” 

Output: String and Function '''

# Given sentence
input_string = "String and String Function"

# Splitting the sentence into words
saperate_string = input_string.split()  # ['String', 'and', 'String', 'Function']

# List to store unique words
string_list = []

# Checking each word
for item in saperate_string:
    if item not in string_list:  # If the word is not already in the list, add it
        string_list.append(item)

# Joining the list back into a sentence
new_string = ' '.join(string_list)

# Output result
print(new_string)  # Output: String and Function

'''
   Output 
String and Function
'''