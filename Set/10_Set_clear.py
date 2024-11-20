'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to clear a set
'''

def clear_set(input_set):
    """
        Description :
            This function clears all items from the given set.
        Parameters :
            input_set: The set to be cleared.
        Return :
            An empty set.
    """
    input_set.clear()
    return input_set

def main():
    sample_set = {1, 2, 3, 4, 5}
    print("Original Set:")
    print(sample_set)
    cleared_set = clear_set(sample_set)
    print("Set after clearing:")
    print(cleared_set)

if __name__ == "__main__":
    main()