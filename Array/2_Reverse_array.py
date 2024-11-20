'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to reverse the order of items in an array.
'''

import array

def create_and_reverse_array():
    """
        Description:
            This function creates an array of integers, displays the array items, 
            and then reverses the order of the items in the array.
        Return:
            None
    """
    int_array = array.array('i', [10, 20, 30, 40, 50])
    print("Original Array items:")
    for item in int_array:
        print(item, end=' ')
    print()
    int_array.reverse()
    print("Reversed Array items:")
    for item in int_array:
        print(item, end=' ')

def main():
    create_and_reverse_array()

if __name__ == "__main__":
    main()