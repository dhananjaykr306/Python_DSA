'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to append a list to the second list
'''

def append_to_list(list1, list2):
    """
        Description:
            This function appends the elements of list1 to list2.
        Parameters:
            list1: The list to be appended.
            list2: The list to which elements will be appended.
        Return:
            The modified list2 after appending elements from list1.
    """
    list2.extend(list1)
    return list2

def main():
    list1 = [4, 5, 6]
    list2 = [1, 2, 3]
    print("list 1 : ")
    print(list1)
    print("list 2 (before appending) : ")
    print(list2)
    modified_list2 = append_to_list(list1, list2)
    print("List 2 (after appending List 1) : ")
    print(modified_list2)

if __name__ == "__main__":
    main()