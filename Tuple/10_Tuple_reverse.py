'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to reverse a tuple
'''

def reverse_tuple(sample_tuple):
    """
        Description :
            This function reverses the given tuple.
        Parameters :
            sample_tuple: The original tuple to be reversed.
        Return :
            A new tuple that is the reverse of the original tuple.
    """
    return sample_tuple[::-1]

def main():
    sample_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("original tuple:")
    print(sample_tuple)
    reversed_tuple = reverse_tuple(sample_tuple)
    print("reversed tuple:")
    print(reversed_tuple)

if __name__ == "__main__":
    main()