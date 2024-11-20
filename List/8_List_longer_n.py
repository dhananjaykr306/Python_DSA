'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to find words longer than n from a given list
'''

def words_longer_than_n(word_list, n):
    """
        Description :
            This function returns a list of words that are longer than n characters from the given list.
        Parameters :
            word_list: The list of words to be filtered.
            n: The length threshold.
        Return :
            A list of words longer than n characters.
    """
    return [word for word in word_list if len(word) > n]  # List comprehension to filter words

def main():
    # Sample list of words
    sample_words = ["apple", "banana", "cherry", "date", "fig", "grape", "kiwi"]
    n = int(input("enter the no : "))
    print("Original List of Words:")
    print(sample_words)
    longer_words = words_longer_than_n(sample_words, n)
    print(f"Words longer than {n} characters:")
    print(longer_words)

if __name__ == "__main__":
    main()