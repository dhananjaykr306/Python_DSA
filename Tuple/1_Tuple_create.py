'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to create a tuple
'''

def create_tuple():
    """
        Description :
            This function creates a tuple with some sample elements.
        Return :
            A tuple with the given elements.
    """
    sample_tuple = (10, 20, 30, 40, 50,60)
    return sample_tuple

def main():
    my_tuple = create_tuple()
    print("created tuple:")
    print(my_tuple)

if __name__ == "__main__":
    main()