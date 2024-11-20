'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to add a key to a dictionary.
'''


def add_key_to_dictionary(dictionary, key, value):
    """
        Description:
            This function adds a key-value pair to a dictionary.
        Parameter:
            dictionary (dict): The dictionary to which the key-value pair will be added.
            key: The key to add to the dictionary.
            value: The value to associate with the key.
        Returns:
            dict: The updated dictionary with the new key-value pair added.
    """
    try:
        dictionary[key] = value
        return dictionary
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    sample_dict = {0: 10, 1: 20}
    print("Original Dictionary:", sample_dict)
    key_to_add = 2
    value_to_add = 30
    updated_dict = add_key_to_dictionary(sample_dict, key_to_add, value_to_add)
    print("Updated Dictionary:", updated_dict)


if __name__ == "__main__":
    main()
