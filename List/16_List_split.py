'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to split a list based on the first character of words
'''

def split_list_by_first_character(words):
    """
        Description:
            This function splits a list of words based on the first character of each word.
        Parameters:
            words: A list of words to be split.
        Return:
            A dictionary where the keys are the first characters and the values are lists of words.
    """
    result = {}
    for word in words:
        first_char = word[0]
        if first_char not in result:
            result[first_char] = []
        result[first_char].append(word)
    return result

def main():
    words = ['apple', 'banana', 'apricot', 'blueberry', 'cherry', 'avocado', 'carrot']
    print("Original List of Words:")
    print(words)
    split_result = split_list_by_first_character(words)
    print("Split List by First Character:")
    for key, value in split_result.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()