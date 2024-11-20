'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to get the smallest number from a list
'''

def get_smallest_number(input_list):
    """
        Description :
            This function returns the smallest number from a list.
        Parameters :
            input_list: The list of numbers to find the smallest number from.
        Return :
            The smallest number in the list.
    """
    return min(input_list) 

def main():
    sample_list = [23, 45, 12, 67, 34, 89, 5]
    print("Sample List:")
    print(sample_list)
    smallest_number = get_smallest_number(sample_list)
    print("Smallest number in the list:", smallest_number)

if __name__ == "__main__":
    main()