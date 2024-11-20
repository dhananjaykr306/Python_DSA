'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python program to count the number of characters (character frequency) in a string
'''

def count_character_frequency(input_string):
    """
        Description :
            This function counts the frequency of each character in the given string.
        Parameters :
            input_string: The string for which to count character frequency.
        Return :
            A dictionary with characters as keys and their frequencies as values.
    """
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

def main():
    sample_string = "google.com"
    print(f"Sample String: {sample_string}")
    result = count_character_frequency(sample_string)
    print("\nCharacter Frequency:")
    print(result)

if __name__ == "__main__":
    main()