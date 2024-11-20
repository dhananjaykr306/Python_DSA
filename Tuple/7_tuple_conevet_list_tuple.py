'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to convert a list to a tuple
'''

def convert_list_to_tuple(sample_list):
    """
        Description :
            This function converts a given list to a tuple.
        Parameters :
            sample_list: The list to be converted to a tuple.
        Return :
            A tuple converted from the input list.
    """
    return tuple(sample_list)

def main():
    sample_list = [1, 2, 3, 4, 5]
    print("Original List:")
    print(sample_list)
    converted_tuple = convert_list_to_tuple(sample_list)
    print("converted tuple:")
    print(converted_tuple)

if __name__ == "__main__":
    main()