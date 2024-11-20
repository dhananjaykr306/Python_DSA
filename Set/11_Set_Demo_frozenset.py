'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to demonstrate the use of frozensets
'''

def demonstrate_frozensets():
    """
        Description :
            This function demonstrates the use of frozensets in Python.
        It shows how to create frozensets, perform operations, and their immutability.
    """
    frozenset_a = frozenset([1, 2, 3, 4, 5])
    frozenset_b = frozenset([4, 5, 6, 7, 8])
    print("Frozenset A:", frozenset_a)
    print("Frozenset B:", frozenset_b)
    union_frozenset = frozenset_a.union(frozenset_b)
    intersection_frozenset = frozenset_a.intersection(frozenset_b)
    difference_frozenset = frozenset_a.difference(frozenset_b)
    print("\nUnion of Frozenset A and Frozenset B:")
    print(union_frozenset)
    print("\nIntersection of Frozenset A and Frozenset B:")
    print(intersection_frozenset)
    print("\nDifference of Frozenset A and Frozenset B (Frozenset A - Frozenset B):")
    print(difference_frozenset)
    try:
        frozenset_a.add(6)
    except AttributeError as e:
        print("\nError:", e)

def main():
    demonstrate_frozensets()

if __name__ == "__main__":
    main()