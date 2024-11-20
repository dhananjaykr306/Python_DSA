'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to create the clone of a tuple
'''

def slice_tuple(sample_tuple):
    """
        Description :
            This function returns a slice (colon) of the tuple from the given start to end index.
        Parameters :
            sample_tuple: The original tuple to slice.
            start: The starting index of the slice.
            end: The ending index of the slice.
        Return :
            A sliced tuple from start to end index.
    """
    return sample_tuple[:]

def main():
    sample_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("original Tuple:")
    print(sample_tuple)
    sliced_tuple = slice_tuple(sample_tuple)
    print("clone Tuple :")
    print(sliced_tuple)

if __name__ == "__main__":
    main()