'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to print all unique values from a list of dictionaries
'''

def unique_values(data):
    """
        Description :
            This function returns all unique values from a list of dictionaries.
        Parameters :
            data: List of dictionaries from which unique values need to be extracted.
        Return :
            It returns a set of unique values.
    """
    return set(value for dic in data for value in dic.values())


def main():
    data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
            {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
    
    unique_vals = unique_values(data)
    print(f"Unique Values: {unique_vals}")


if __name__ == "__main__":
    main()