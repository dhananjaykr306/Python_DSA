'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to remove item(s) from a set
'''

def remove_items_from_set(input_set, items_to_remove):
    """
        Description :
            This function removes specified items from a set.
        Parameters :
            input_set: The set from which items will be removed.
            items_to_remove: A list of items to remove from the set.
        Return :
            It returns the updated set.
    """
    for item in items_to_remove:
        input_set.discard(item)
    return input_set

def main():
    sample_set = {1, 2, 3, 4, 5}
    items_to_remove = [3, 4, 6]

    print("Original Set:")
    print(sample_set)
    updated_set = remove_items_from_set(sample_set, items_to_remove)
    print("Updated Set after removing items:")
    print(updated_set)

if __name__ == "__main__":
    main()