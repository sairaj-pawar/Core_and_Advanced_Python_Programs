#Assignment 2 -Write a Python program to get the largest and smallest number from a list without built in functions.

List = [4, 5, 6, 8, 2]  
Sorted_array = []  # Empty list to store sorted numbers

# Sorting the list manually using a while loop
while List:
    Smallest = List[0]  # Assume the first element is the smallest
    for num in List:
        if num < Smallest:  # Find the smallest number
            Smallest = num  
    Sorted_array.append(Smallest)  # Add the smallest number to sorted list
    List.remove(Smallest)  # Remove the smallest number from the original list

# Get the smallest and largest numbers
Smallest_number = Sorted_array[0]  # First element is the smallest
Largest_number = Sorted_array[-1]  # Last element is the largest

# Print the results
print("Sorted Array:", Sorted_array)  
print("Smallest Number:", Smallest_number)  
print("Largest Number:", Largest_number)

''' Output:
Sorted Array: [2, 4, 5, 6, 8]  
Smallest Number: 2  
Largest Number: 8  
'''

