'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to iterate over dictionaries using for loops.
'''


def iterate_dictionary(sample_dict):
    """
        Description:
            This function iterates over a dictionary and prints its keys and values.
        Parameters:
            sample_dict : The dictionary to iterate over.
    """
    print("Iterating over keys:")
    for key in sample_dict:
        print(f"Key: {key}")
    print("\nIterating over values:")
    for value in sample_dict.values():
        print(f"Value: {value}")
    print("\nIterating over key-value pairs:")
    for key, value in sample_dict.items():
        print(f"Key: {key}, Value: {value}")


def main():
    sample_dict = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
    iterate_dictionary(sample_dict)

if __name__ == "__main__":
    main()