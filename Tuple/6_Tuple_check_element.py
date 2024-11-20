'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to check whether an element exists within a tuple
'''

def check_element_in_tuple(sample_tuple, element):
    """
        Description :
            This function checks if a given element exists in the tuple.
        Parameters :
            sample_tuple: The tuple in which to check for the element.
            element: The element to search for in the tuple.
        Return :
            True if the element is found, otherwise False.
    """
    if element in sample_tuple:
        return True
    else:
        return False

def main():
    sample_tuple = (10, 20, 30, 40, 50)
    element_to_check = 30
    print("Original Tuple:")
    print(sample_tuple)
    exists = check_element_in_tuple(sample_tuple, element_to_check)
    if exists:
        print(f"\nElement {element_to_check} exists in the tuple.")
    else:
        print(f"\nElement {element_to_check} does not exist in the tuple.")

if __name__ == "__main__":
    main()