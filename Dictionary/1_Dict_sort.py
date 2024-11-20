'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to sort a dictionary by value.
'''


def sort_dictionary(data):
    """
        Description:
            This function sorts a dictionary by its values in both ascending 
            and descending order and prints the results.
        parameter:data dictionary
        return the sorted dictionary by item
    """
    try:
        sorted_ascending = dict(sorted(data.items(), key=lambda item: item[1]))
        print("Sorted in ascending order:", sorted_ascending)
        sorted_descending = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
        print("Sorted in descending order:", sorted_descending)

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    data = {
        'apple': 5,
        'banana': 2,
        'orange': 8,
        'grape': 1,
        'kiwi': 4
    }
    sort_dictionary(data)

if __name__ == "__main__":
    main()