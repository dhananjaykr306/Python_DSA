'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to create set difference
'''

def difference_of_sets(set1, set2):
    """
        Description :
            This function returns the difference of two sets.
        Parameters :
            set1: The first set (minuend).
            set2: The second set (subtrahend).
        Return :
            A set containing elements that are in set1 but not in set2.
    """
    return set1.difference(set2)

def main():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print("Set A:", set_a)
    print("Set B:", set_b)
    difference_set = difference_of_sets(set_a, set_b)
    print("Difference of Set A and Set B (Set A - Set B):")
    print(difference_set)

if __name__ == "__main__":
    main()