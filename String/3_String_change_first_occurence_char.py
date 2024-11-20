'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to replace occurrences of the first character in a string
'''

def replace_first_char(input_string):
    """
        Description :
            This function replaces all occurrences of the first character in the string
            with '$', except for the first occurrence itself.
        Parameters :
            input_string: The string to process.
        Return :
            A new string with the first character replaced as specified.
    """
    if not input_string: 
        return input_string    
    first_char = input_string[0]
    modified_string = first_char + input_string[1:].replace(first_char, '$')
    return modified_string

def main():
    sample_string = "restart"
    print(f"Sample String: {sample_string}")
    result = replace_first_char(sample_string)
    print("\nModified String:")
    print(result)

if __name__ == "__main__":
    main()