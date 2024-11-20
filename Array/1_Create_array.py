'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to create an array of integers and display the array items.
'''

import array

def create_and_display_array():
    """
        Description:
            This function creates an array of 5 integers and displays the array items.
        Return:
            None
    """
    # Creating an array of 5 integers
    int_array = array.array('i', [10, 20, 30, 40, 50])
    
    # Displaying the array items
    print("Array items:")
    for item in int_array:
        print(item, end=' ')
    print()  # For a new line

    # Accessing individual elements through indexes
    print("Accessing individual elements:")
    for index in range(len(int_array)):
        print(f"Element at index {index}: {int_array[index]}")

def main():
    create_and_display_array()

if __name__ == "__main__":
    main()