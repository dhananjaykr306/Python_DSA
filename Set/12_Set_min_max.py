'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to find maximum and minimum value in a set
'''

def find_max_min(input_set):
    """
        Description :
            This function finds the maximum and minimum values in a given set.
        Parameters :
            input_set: The set from which to find max and min values.
        Return :
            A tuple containing the maximum and minimum values.
    """
    max_value = max(input_set)  
    min_value = min(input_set)  
    return max_value, min_value

def main():
    sample_set = {10, 20, 5, 30, 15}
    print("Sample Set:", sample_set)
    max_value, min_value = find_max_min(sample_set)
    print("Maximum Value in the Set:", max_value)
    print("Minimum Value in the Set:", min_value)

if __name__ == "__main__":
    main()