'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program which accepts a sequence of comma-separated numbers from user and generates a list and a tuple with those numbers.
'''

def Lst(values):
    """
        Description :
            This function is used to return a list
        Parameters :
            values: This is the list of comma-separated values received from user
        Return :
            It returns the list of the values
    """
    return list(values)

def tuples(values):
    """
        Description :
            This function is used to return a tuple
        Parameters :
            values: This is the list of comma-separated values received from user
        Return :
            It returns the tuple of the values
    """
    return tuple(values)

def main():
    values = input("Enter comma-separated values: ").split(',')
    print(f"List = {Lst(values)}")
    print(f"Tuple = {tuples(values)}")

if __name__=="__main__":
    main()