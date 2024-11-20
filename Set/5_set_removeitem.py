'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to remove an item from a set if it is present
'''

def remove_item_if_present(input_set, item):
    """
        Description :
            This function removes an item from the set if it is present.
        Parameters :
            input_set: The set from which the item will be removed.
            item: The item to remove from the set.
        Return :
            It returns the updated set.
    """
    if item in input_set:
        input_set.remove(item)
        print(f"Item '{item}' removed from the set.")
    else:
        print(f"Item '{item}' not found in the set.")
    return input_set

def main():
    sample_set = {1, 2, 3, 4, 5}
    print("Original Set:")
    print(sample_set)
    item_to_remove = int(input("Enter the item to remove : "))
    updated_set = remove_item_if_present(sample_set, item_to_remove)
    print("Updated Set after attempting to remove the item:")
    print(updated_set)

if __name__ == "__main__":
    main()