'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to sort a list of tuples by the last element
'''

def sort_tuples_by_last_element(tuples_list):
    """
        Description :
            This function sorts a list of non-empty tuples in increasing order by the last element
            in each tuple.
        Parameters :
            tuples_list: The list of non-empty tuples to be sorted.
        Return :
            A sorted list of tuples.
    """
    return sorted(tuples_list, key=lambda x: x[-1])

def main():
    sample_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print("sample list:")
    print(sample_list)
    sorted_list = sort_tuples_by_last_element(sample_list)
    print("sorted list by the last element in each tuple:")
    print(sorted_list)

if __name__ == "__main__":
    main()