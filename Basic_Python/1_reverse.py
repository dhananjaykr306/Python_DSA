'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program which accepts the user's first and last name and print them in reverse order with a space between them.

'''

def reverseName(f_name,l_name):
    """
        Description :
            This function is used to return reverse of f_name,l_name
        Parameters :
            f_name,l_name: This is the f_name that we have to reverse, l_name that we have to reverse
        Return :
            It returns reverse of the l_name+" " +f_name
    """
    return l_name +" "+f_name
    

def main():
    f_name = input("Enter a f_name : ")
    l_name = input("Enter the last_name : " )
    rev = reverseName(f_name,l_name)
    print(f"Reverse of {f_name} and {l_name} is {rev}")

if __name__=="__main__":
    main()