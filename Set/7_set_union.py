'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to create a union of sets
'''

def union_of_sets(set1, set2):
    """
        Description :
            This function returns the union of two sets.
        Parameters :
            set1: The first set.
            set2: The second set.
        Return :
            A set containing all unique elements from set1 and set2.
    """
    return set1.union(set2)

def main():
    # Sample sets
    set_a = {1, 2, 3, 4, 5}
    set_b = {4, 5, 6, 7, 8}
    print("Set A:", set_a)
    print("Set B:", set_b)
    union_set = union_of_sets(set_a, set_b)
    print("Union of Set A and Set B:")
    print(union_set)

if __name__ == "__main__":
    main()