'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to remove specified elements from a list
'''

def remove_elements(input_list):
    """
        Description :
            This function removes the elements at the specified indices from the list.
        Parameters :
            input_list: The list from which elements are to be removed.
        Return :
            A new list after removing the specified elements.
    """
    return [input_list[i] for i in range(len(input_list)) if i not in (0, 4, 5)]

def main():
    sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print("Original List:")
    print(sample_list)
    modified_list = remove_elements(sample_list)
    print("list after removing the 0th, 4th, and 5th elements:")
    print(modified_list)

if __name__ == "__main__":
    main()