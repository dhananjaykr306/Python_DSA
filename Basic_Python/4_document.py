'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program to print the documents (syntax, description, etc.) of Python built-in function(s).
'''

def print_function_docs(func):
    """
        Description :
            This function is used to print the documentation of any Python built-in function.
        Parameters :
            func : The built-in function whose documentation will be printed.
        Return :
            None
    """
    print(f"Documentation for {func.__name__}:\n")
    print(func.__doc__)

def main():
    #x = input("Enter the built in function : ")
    print_function_docs(abs)

if __name__=="__main__":
    main()