'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to get the last part of a string before a specified character
'''

def get_last_part_before_char(input_string, delimiter):
    """
        Description :
            This function returns the last part of a string before the specified character.
        Parameters :
            input_string: The input string to process.
            delimiter: The character before which we want to find the last part.
        Return :
            The last part of the string before the specified character.
    """
    index = input_string.rfind(delimiter) 
    if index != -1:
        return input_string[index:]  
    return input_string  

def main():
    user_input = input("Enter a string: ")  
    delimiter = input("Enter the delimiter character: ")  
    result = get_last_part_before_char(user_input, delimiter)
    print(f"\nLast part of the string before '{delimiter}' : '{result}'")

if __name__ == "__main__":
    main()