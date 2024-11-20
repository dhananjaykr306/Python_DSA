'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to remove duplicates from a list
'''

def remove_duplicates(input_list):
    """
        Description :
            This function removes duplicates from a list.
        Parameters :
            input_list: The list from which duplicates need to be removed.
        Return :
            A list with duplicates removed.
    """
    return list(set(input_list))

def main():
    sample_list = [1, 2, 3, 2, 4, 1, 5, 3, 6, 4]
    print("sample list:")
    print(sample_list)
    unique_list = remove_duplicates(sample_list)
    print("list after removing duplicates:")
    print(unique_list)

if __name__ == "__main__":
    main()