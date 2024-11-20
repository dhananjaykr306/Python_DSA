'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to find the repeated items of a tuple
'''

def find_repeated_items(sample_tuple):
    """
        Description :
            This function finds and returns the repeated items in the given tuple.
        Parameters :
            sample_tuple: The tuple in which repeated items are to be found.
        Return :
            A set containing the repeated items.
    """
    repeated_items = set([item for item in sample_tuple if sample_tuple.count(item) > 1])
    return repeated_items

def main():
    sample_tuple = (1, 2, 3, 4, 5, 2, 6, 7, 8, 3, 9, 10, 5)
    print("Original Tuple:")
    print(sample_tuple)
    repeated = find_repeated_items(sample_tuple)
    print("\nRepeated Items in the Tuple:")
    print(repeated)

if __name__ == "__main__":
    main()