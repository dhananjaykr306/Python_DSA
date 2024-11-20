'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program to check whether a file exists.
'''

import os

def check_file_exists(file_name):
    """
        Description :
            This function checks if a file exists in the current directory.
        Parameters :
            file_name : The name of the file to check.
        Return :
            True if the file exists, otherwise False.
    """
    return os.path.exists(file_name)

def main():
    file_name = input("Enter the file name (with extension) to check: ")
    if check_file_exists(file_name):
        print(f"The file '{file_name}' exists.")
    else:
        print(f"The file '{file_name}' does not exist.")

if __name__ == "__main__":
    main()