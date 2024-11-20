'''
    @Author: Dhananjay Kumar
    @Date: 08-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 08-10-2024
    @Title : Python program to multiply all the items in a list
'''

def multiply_list_items(input_list):
    """
        Description :
            This function multiplies all items in a list.
        Parameters :
            input_list: The list of numbers to be multiplied.
        Return :
            The product of all items in the list.
    """
    product = 1 
    for item in input_list:
        product *= item  
    return product

def main():
    sample_list = [1, 2, 3, 4, 5]
    print("Sample List:")
    print(sample_list)
    total_product = multiply_list_items(sample_list)
    print("Product of all items in the list:", total_product)

if __name__ == "__main__":
    main()