'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to unpack a tuple into several variables
'''

def unpack_tuple(sample_tuple):
    """
        Description :
            This function unpacks a tuple into separate variables.
        Parameters :
            sample_tuple: A tuple to be unpacked.
    """
    a, b, c, d, e = sample_tuple
    print("Unpacked Values:")
    print(f"a = {a}, b = {b}, c = {c}, d = {d}, e = {e}")

def main():
    sample_tuple = (10, "Python", 3.14, False, [1, 2, 3])
    print("Original Tuple:")
    print(sample_tuple)
    
    # Unpacking the tuple into several variables
    unpack_tuple(sample_tuple)

if __name__ == "__main__":
    main()