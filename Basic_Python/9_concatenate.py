'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program to concatenate all elements in a list into a string and return it.
'''

def concatenate_list_elements(values_list):
    """
        Description :
            This function concatenates all elements in a list into a single string.
        Parameters :
            values_list : The list of strings to be concatenated.
        Return :
            A single concatenated string.
    """
    return ''.join(values_list)

def main():
    values = input("Enter the group of strings (comma-separated): ").split(',')
    values_list = [value for value in values]
    concatenated_string = concatenate_list_elements(values_list)
    print(f"Concatenated string: {concatenated_string}")

if __name__ == "__main__":
    main()