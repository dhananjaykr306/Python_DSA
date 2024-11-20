'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python function to check if two lists have at least one common member
'''

def have_common_member(list1, list2):
    """
        Description :
            This function checks if there is at least one common member in two lists.
        Parameters :
            list1: The first list.
            list2: The second list.
        Return :
            True if there is at least one common member, False otherwise.
    """
    set_list2 = set(list2)
    for item in list1:
        if item in set_list2:
            return True      
    return False

def main():
    list1 = [1, 2, 3, 4, 5]
    list2 = [5, 6, 7, 8, 9]
    print("List 1:")
    print(list1)
    print("List 2:")
    print(list2)
    result = have_common_member(list1, list2)
    print("Do the two lists have at least one common member?")
    print(result)

if __name__ == "__main__":
    main()