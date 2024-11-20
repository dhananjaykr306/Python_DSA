'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to create a dictionary from a string, tracking letter counts.
'''


def create_dict_from_string(string):
    """
        Description:
            This function creates a dictionary from a string, where the keys are
            the characters from the string, and the values are their respective counts.
        Parameter:
            string (str): The input string.
        Returns:
            dict: A dictionary with characters as keys and their counts as values.
    """
    try:
        char_count = {}
        for char in string:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def main():
    sample_string = "w3resource"
    print("Sample String:", sample_string)
    result = create_dict_from_string(sample_string)
    print("Resultant Dictionary:", result)


if __name__ == "__main__":
    main()
