'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to remove a key from a dictionary.
'''


def remove_key_from_dict(sample_dict, key_to_remove):
    """
        Description:
            This function removes a specified key from the dictionary.
        Parameters:
            sample_dict : The dictionary from which the key will be removed.
            key_to_remove : The key that needs to be removed from the dictionary.
        Return:
            The updated dictionary after the key has been removed.
    """
    if key_to_remove in sample_dict:
        del sample_dict[key_to_remove]
        print(f"Key '{key_to_remove}' has been removed.")
    else:
        print(f"Key '{key_to_remove}' not found in the dictionary.")
    
    return sample_dict
    

def main():
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }    
    print("Original Dictionary:", sample_dict)
    key_to_remove = input("enter the key to remove : ")
    updated_dict = remove_key_from_dict(sample_dict, key_to_remove)
    print("Updated Dictionary:", updated_dict)

if __name__ == "__main__":
    main()