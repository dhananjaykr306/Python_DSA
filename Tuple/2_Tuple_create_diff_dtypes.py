'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to create a tuple with different data types
'''

def create_mixed_tuple():
    """
        Description :
            This function creates a tuple with elements of different data types.
        Return :
            A tuple with elements of various data types.
    """ 
    mixed_tuple = (1, "Hello", 3.14, True, [10, 20, 30])
    return mixed_tuple

def main():
    my_tuple = create_mixed_tuple()
    print("tuple with different data type : ")
    print(my_tuple)

if __name__ == "__main__":
    main()