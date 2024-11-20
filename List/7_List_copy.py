'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to clone or copy a list
'''

def clone_list(original_list):
    """
        Description :
            This function creates a clone of the given list.
        Parameters :
            original_list: The list to be cloned.
        Return :
            A new list that is a clone of the original list.
    """
    return original_list[:]

def main():
    sample_list = [1, 2, 3, 4, 5]
    print("original list:")
    print(sample_list)
    cloned_list = clone_list(sample_list)
    print("cloned list:")
    print(cloned_list)

if __name__ == "__main__":
    main()