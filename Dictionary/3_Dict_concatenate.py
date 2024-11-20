'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to concatenate multiple dictionaries.
'''

def concatenate_dicts(*dicts):
    """
        Description:
            This function concatenates multiple dictionaries into one.
        Parameters:
            *dicts : Variable number of dictionaries to concatenate.
        Return:
            A new dictionary that contains all the key-value pairs from the input dictionaries.
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result


def main():
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}
    concatenated_dict = concatenate_dicts(dic1, dic2, dic3)
    print("Concatenated Dictionary:", concatenated_dict)

if __name__ == "__main__":
    main()