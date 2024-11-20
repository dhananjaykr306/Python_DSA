'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title: Python program to generate a dictionary with numbers and their squares.
'''

def generate_square_dict(n):
    """
        Description:
            This function generates a dictionary with numbers (from 1 to n) as keys 
            and their squares as values.
        Parameters:
            n : The upper limit of numbers.
        Return:
            A dictionary containing numbers and their squares.
    """
    square_dict = {x: x * x for x in range(1, n + 1)} 
    return square_dict


def main():
    n = 5
    result_dict = generate_square_dict(n)
    print("Generated Dictionary:", result_dict)


if __name__ == "__main__":
    main()