'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program to create a histogram from a given list of integers.
'''

def create_histogram(values_list):
    """
        Description :
            This function creates a histogram from a given list of integers by printing '*' characters.
        Parameters :
            values_list : The list of integers representing the histogram.
        Return :
            None
    """
    for value in values_list:
        print(f"{value}  :  {'*' * value}")

def main():
    values = input("Enter the group of integers (comma-separated): ").split(',')
    values_list = list(map(int, values))
    create_histogram(values_list)

if __name__ == "__main__":
    main()