'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to count strings with the same first and last character
'''

def count_strings(input_list):
    """
        Description :
            This function counts the number of strings where the string length is 2 or more
            and the first and last character are the same.
        Parameters :
            input_list: The list of strings to be checked.
        Return :
            The count of strings meeting the criteria.
    """
    count = 0
    for string in input_list:
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1
    return count

def main():
    sample_list = ['abc', 'xyz', 'aba', '1221']
    print("Sample List:")
    print(sample_list)
    result = count_strings(sample_list)
    print("Number of strings where the length is 2 or more and first and last character are the same:", result)

if __name__ == "__main__":
    main()