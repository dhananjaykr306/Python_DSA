'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to iterate over sets
'''

def iterate_over_set(input_set):
    """
        Description :
            This function iterates over a set and prints each element.
        Parameters :
            input_set: The set to iterate over.
        Return :
            It returns nothing, just prints the elements of the set.
    """
    for item in input_set:
        print(item)

def main():
    sample_set = {10, 20, 30, 40, 50}
    print("Iterating over the set:")
    iterate_over_set(sample_set)

if __name__ == "__main__":
    main()