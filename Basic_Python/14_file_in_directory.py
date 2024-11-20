'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to list all files in a directory.
'''

import os

def list_files_in_directory(directory):
    """
        Description:
            This function lists all files in the specified directory.
        Parameters:
            directory: The path of the directory to list files from.
        Return:
            A list of files in the specified directory.
    """
    try:
        entries = os.listdir(directory)
        # Filter the files from the entries
        files = [entry for entry in entries if os.path.isfile(os.path.join(directory, entry))]
        return files
    except Exception as e:
        print(f"serror occurred: {e}")
        return []

def main():
    directory = input("enter the directory path: ")
    files = list_files_in_directory(directory)
    if files:
        print(f"files in '{directory}':")
        for file in files:
            print(file)
    else:
        print(f"no files found in '{directory}' or the directory does not exist.")

if __name__ == "__main__":
    main()