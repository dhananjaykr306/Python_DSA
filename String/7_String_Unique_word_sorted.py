'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to print unique words in sorted order from user input
'''

def unique_sorted_words(input_string):
    """
        Description :
            This function takes a comma-separated string of words and returns a 
            sorted list of unique words.
        Parameters :
            input_string: A string of comma-separated words.
        Return :
            A sorted list of unique words.
    """
    words = set(word.strip() for word in input_string.split(','))
    sorted_words = sorted(words)
    return sorted_words

def main():
    user_input = input("Enter a comma-separated sequence of words: ")  # Accept user input
    print("sample words:", user_input)
    result = unique_sorted_words(user_input)
    print("unique sorted words:", ', '.join(result))

if __name__ == "__main__":
    main()
