'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to calculate the length of a string
'''

def calculate_string_length(input_string):
    """
        Description :
            This function calculates and returns the length of the given string.
        Parameters :
            input_string: The string whose length is to be calculated.
        Return :
            The length of the input string.
    """
    return len(input_string)

def main():
    user_input = input("Enter a string: ")
    length_of_string = calculate_string_length(user_input)
    print(f"The length of the entered string is: {length_of_string}")

if __name__ == "__main__":
    main()