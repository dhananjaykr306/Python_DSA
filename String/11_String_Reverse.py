'''
    @Author: Dhananjay Kumar
    @Date: 10-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 10-10-2024 
    @Title : Python program to reverse a string
'''

def reverse_string(input_string):
    """
        Description :
            This function returns the reversed version of the input string.
        Parameters :
            input_string: The string to reverse.
        Return :
            The reversed string.
    """
    words = input_string.split()
    words = words[::-1]
    reverse_string = " ".join(word for word in words)
    return reverse_string[::-1]

def main():
    user_input = input("Enter a string to reverse: ")  
    reversed_string = reverse_string(user_input)  
    print(f"Reversed String: '{reversed_string}'")

if __name__ == "__main__":
    main()