#Assignement 3 - Write a Python program to find duplicate values from a list and display those.
# Define the list of numbers
List = [2, 3, 3, 4, 5, 6]

# Empty lists to store unique numbers and duplicate numbers
Empty_list = []
Duplicate_list = []

# Loop through the list to find duplicates
for num in List:
    if num not in Empty_list:  # If the number is not already in Empty_list
        Empty_list.append(num)  # Add it to Empty_list (unique numbers)
    elif num in Empty_list:  # If the number is already in Empty_list
        if num not in Duplicate_list:  # Ensure duplicates are added only once
            Duplicate_list.append(num)  # Add to Duplicate_list

# Print the duplicate values
print("Duplicate values in the list:", Duplicate_list)

''' 
 Output:
Duplicate values in the list: [3]
'''
