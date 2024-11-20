'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to count the number of items in dictionary values that are lists
'''


def count_items_in_list_values(data_dict):
    """
        Description :
            This function counts the number of items in dictionary values that are lists.
        Parameters :
            data_dict: The dictionary to process.
        Return :
            It returns a dictionary where keys are the original keys and values are the counts of items in the lists.
    """
    count_dict = {}
    for key, value in data_dict.items():
        if isinstance(value, list):
            count_dict[key] = len(value)
    return count_dict

def main():
    sample_dict = {'fruits': ['apple', 'banana', 'cherry'], 
                   'vegetables': ['carrot', 'broccoli'], 
                   'numbers': [1, 2, 3, 4, 5], 
                   'name': 'John'}
    result = count_items_in_list_values(sample_dict)
    print("Count of items in dictionary values that are lists:")
    print(result)


if __name__ == "__main__":
    main()