'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to check if multiple keys exist in a dictionary
'''


def check_keys_exist(data_dict, keys):
    """
        Description :
            This function checks whether multiple keys exist in a dictionary.
        Parameters :
            data_dict: The dictionary in which to check the keys.
            keys: A list of keys to check for existence in the dictionary.
        Return :
            It returns True if all keys exist, otherwise False.
    """
    return all(key in data_dict for key in keys)

def main():
    sample_dict = {'id': 1, 'name': 'John', 'age': 25, 'success': True}
    keys_to_check = ['id', 'name']
    result = check_keys_exist(sample_dict, keys_to_check)
    print(f"All keys {keys_to_check} exist in dictionary: {result}")
    

if __name__ == "__main__":
    main()