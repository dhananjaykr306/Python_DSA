'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to remove an item from a tuple
'''

def remove_item_from_tuple(sample_tuple, item):
    """
        Description :
            This function removes the first occurrence of an item from a tuple.
        Parameters :
            sample_tuple: The tuple from which to remove the item.
            item: The item to remove from the tuple.
        Return :
            A new tuple with the item removed.
    """
    temp_list = list(sample_tuple)
    try:
        temp_list.remove(item)
    except ValueError:
        print(f"Item {item} not found in the tuple.")
    return tuple(temp_list)

def main():
    sample_tuple = (1, 2, 3, 4, 5)
    item_to_remove = 3
    print("Original Tuple:")
    print(sample_tuple)
    modified_tuple = remove_item_from_tuple(sample_tuple, item_to_remove)
    print("\nTuple after removing item:")
    print(modified_tuple)

if __name__ == "__main__":
    main()