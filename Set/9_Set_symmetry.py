'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to create a symmetric difference
'''

def symmetric_difference_of_sets(set1, set2):
    """
        Description :
            This function returns the symmetric difference of two sets.
        Parameters :
            set1: The first set.
            set2: The second set.
        Return :
            A set containing elements that are in either set1 or set2 but not in both.
    """
    return set1.symmetric_difference(set2)

def main():
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print("Set A:", set_a)
    print("Set B:", set_b)
    sym_diff_set = symmetric_difference_of_sets(set_a, set_b)
    print("Symmetric Difference of Set A and Set B:")
    print(sym_diff_set)

if __name__ == "__main__":
    main()