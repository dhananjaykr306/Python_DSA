'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to count occurrences of a substring in a string
'''

def count_substring_occurrences(input_string, substring):
    """
        Description :
            This function counts the number of occurrences of a substring in a given string.
        Parameters :
            input_string: The string to search within.
            substring: The substring to count.
        Return :
            The count of occurrences of the substring.
    """
    count = input_string.count(substring)
    return count

def main():
    user_input = input("Enter the main string: ")
    substring = input("Enter the substring to count: ")
    occurrences = count_substring_occurrences(user_input, substring)
    print(f"\nThe substring '{substring}' occurs {occurrences} times in the string.")

if __name__ == "__main__":
    main()