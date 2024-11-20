'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to slice a tuple
'''

def slice_tuple(sample_tuple, start, end):
    """
        Description :
            This function slices a tuple from the given start to end index.
        Parameters :
            sample_tuple: The original tuple to slice.
            start: The starting index of the slice.
            end: The ending index of the slice.
        Return :
            A sliced tuple from start to end index.
    """
    return sample_tuple[start:end]

def main():
    sample_tuple = (10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
    print("Original Tuple:")
    print(sample_tuple)
    sliced_tuple = slice_tuple(sample_tuple, 2, 5)
    print("\nSliced Tuple (from index 2 to 5):")
    print(sliced_tuple)

if __name__ == "__main__":
    main()