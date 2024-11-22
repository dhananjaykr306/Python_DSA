 '''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
 @Title: To Remove first occurence of the specified element in the array problem
'''
import array

def remove_ele(arr,ele):
    """ 
    Description :
        This function is used to remove First occurence of element from the array
    Parameters :
        arr = Array Elements
        ele = Element to be removed from the array
    Return :
            It returns the array after removing the element
    """
    arr.remove(ele)
    for i in range(0,len(arr)):
        print(arr[i],end=' ')

def main():
    arr_ele = array.array('i',[1,4,7,8,4,4,1,7,8,7,6])
    ele_remove = int(input("Enter the element to be removed"))
    remove_ele(arr_ele,ele_remove)

if __name__ == "__main__":
    main()