'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to sum all the items in a list
'''

def sum_of_list(input_list):
    """
        Description :
            This function returns the sum of all items in the given list.
        Parameters :
            input_list: A list of numeric values to be summed.
        Return :
            The sum of all items in the list.
    """
    return sum(input_list)

def main():
    sample_list = [10, 20, 30, 40, 50]
    print("Sample List:")
    print(sample_list)
    total_sum = sum_of_list(sample_list)
    print("Sum of all items in the list:", total_sum)

if __name__ == "__main__":
    main()