'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program to display the first and last colors from the following list.
'''

def display(colors):
    """
        Description :
            This function is used to return the first and last value in the list
        Parameters :
            colors: This is the list of colors received from user
        Return :
            It returns the first and last values
    """
    lst = list(colors)
    return lst[0] +" , "+ lst[-1]

def main():
    values = input("Enter comma-separated values of colors: ").split(',')
    print(f"first,last = {display(values)}")

if __name__=="__main__":
    main()