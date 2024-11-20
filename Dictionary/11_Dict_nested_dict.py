'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to convert a list into a nested dictionary of keys
'''


def list_to_nested_dict(lst):
    """
        Description :
            This function converts a list into a nested dictionary where each element of the list 
            becomes a key in a nested structure.
        Parameters :
            lst: List of elements to be converted into a nested dictionary.
        Return :
            A nested dictionary where each key is nested within the next.
    """
    nested_dict = current = {}
    for item in lst:
        current[item] = {}
        current = current[item]
    return nested_dict


def main():
    data_list = ['a', 'b', 'c', 'd']
    nested_dict = list_to_nested_dict(data_list)
    print("Nested Dictionary:")
    print(nested_dict)


if __name__ == "__main__":
    main()