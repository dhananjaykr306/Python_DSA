'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program to check whether a specified value is contained in a group of values.
'''

def check_value_in_list(value, values_list):
    """
        Description :
            This function checks if a specified value is in the list.
        Parameters :
            value : The value to check.
            values_list : The list of values in which to search.
        Return :
            True if the value is found in the list, otherwise False.
    """
    return value in values_list

def main():
    value = int(input("Enter the value to check: "))
    values = input("Enter the group of values (comma-separated): ").split(',')
    values_list = list(map(int, values))
    result = check_value_in_list(value, values_list)
    print(f"{value} -> {values_list} : {result}")

if __name__ == "__main__":
    main()