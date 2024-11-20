'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by:Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to count how many dictionaries have 'success' as True
'''


def count_true_success(data, key):
    """
        Description :
            This function counts how many dictionaries have the key with value True.
        Parameters :
            data: List of dictionaries.
            key: The key to check for True values.
        Return :
            it returns the count of dictionaries where the value of the key is True.
    """
    return sum(1 for dic in data if dic.get(key) is True)
    

def main():
    data = [{'id': 1, 'success': True, 'name': 'Lary'},
            {'id': 2, 'success': False, 'name': 'Rabi'},
            {'id': 3, 'success': True, 'name': 'Alex'}]    
    key_to_count = "success"
    true_count = count_true_success(data, key_to_count)    
    print(f"Count of dictionaries with '{key_to_count}' as True: {true_count}")

if __name__ == "__main__":
    main()