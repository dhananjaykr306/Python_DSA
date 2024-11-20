'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program to print a set containing colors from color_list_1 not present in color_list_2.
'''

def find_unique_colors(color_list_1, color_list_2):
    """
        Description :
            This function finds colors in color_list_1 that are not in color_list_2.
        Parameters :
            color_list_1 : A set containing the first group of colors.
            color_list_2 : A set containing the second group of colors.
        Return :
            A set containing colors from color_list_1 that are not in color_list_2.
    """
    return color_list_1.difference(color_list_2)

def main():
    # Test data
    color_list_1 = set(["White", "Black", "Red"])
    color_list_2 = set(["Red", "Green"])
    unique_colors = find_unique_colors(color_list_1, color_list_2)
    print(f"Colors in color_list_1 not in color_list_2: {unique_colors}")

if __name__ == "__main__":
    main()