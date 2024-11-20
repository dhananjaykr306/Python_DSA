'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to add 'ing' or 'ly' to a string based on conditions
'''

def modify_string(input_string):
    """
        Description :
            This function adds 'ing' at the end of a string if its length is at least 3.
            If the string ends with 'ing', it adds 'ly' instead. If the length is less than 3, it leaves the string unchanged.
        Parameters :
            input_string: The string to be modified.
        Return :
            The modified string based on the rules.
    """
    if len(input_string) < 3:
        return input_string
    
    if input_string.endswith('ing'):
        return input_string + 'ly'
    else:
        return input_string + 'ing'

def main():
    sample_string1 = "abc"
    sample_string2 = "string"    
    print(f"Sample String 1: {sample_string1}")
    result1 = modify_string(sample_string1)
    print(f"Expected Result: 'abcing', Actual Result: '{result1}'\n")    
    print(f"Sample String 2: {sample_string2}")
    result2 = modify_string(sample_string2)
    print(f"Expected Result: 'stringly', Actual Result: '{result2}'")

if __name__ == "__main__":
    main()