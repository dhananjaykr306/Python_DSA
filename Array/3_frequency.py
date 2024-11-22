'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title:Count the occurence of element in the array problem
'''
import array

def count_ele(arr,ele):
    """ 
    Description :
        This function is used to Count Number of times specified element present in the array
    Parameters :
        arr = Array Elements
        ele = Element to be count
    Return :
            It returns the Count of Element
    """
    ele_val = arr.count(ele)
    return ele_val

def main():
    arr_ele = array.array('i',[1,4,7,8,4,4,1,7,8,7,6])
    ele = int(input("Enter the Element to find"))
    value = count_ele(arr_ele,ele)
    print(f"The Number of times the {ele} present in the array is {value}")

if __name__ == "__main__":
    main()
