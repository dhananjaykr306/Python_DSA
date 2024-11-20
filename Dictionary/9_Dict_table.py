'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to print a dictionary in table format
'''

def print_dict_table(data):
    """
        Description :
            This function prints the dictionary in a table format.
        Parameters :
            data: The dictionary to be printed in table format.
        Return :
            It returns nothing, just prints the table format.
    """
    print(f"{'Key':<15} {'Value':<15}")
    print('-' * 30)
    
    for key, value in data.items():
        print(f"{key:<15} {value:<15}")


def main():
    data = {
        'Name': "Dhananjay",
        'Age': 22,
        'Occupation': 'Engineer',
        'Country': 'INDIA'
    }

    print_dict_table(data)


if __name__ == "__main__":
    main()