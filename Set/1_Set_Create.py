'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to create a set
'''

def create_set(elements):
    """
        Description :
            This function creates a set from a given list of elements.
        Parameters :
            elements: A list of elements to be added to the set.
        Return :
            It returns a set containing unique elements.
    """
    return set(elements)

def main():
    elements = [1, 2, 3, 4, 5, 5, 4, 3, 2, 1]
    unique_set = create_set(elements)
    print("Created Set:")
    print(unique_set)

if __name__ == "__main__":
    main()