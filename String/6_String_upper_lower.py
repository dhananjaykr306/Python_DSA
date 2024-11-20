'''
    @Author: Dhananjay Kumar
    @Date: 09-10-2024 
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 09-10-2024 
    @Title : Python script to convert user input to upper and lower cases
'''

def main():
    user_input = input("Please enter a string: ") 
    upper_case = user_input.upper()
    lower_case = user_input.lower()
    print("original string: ", user_input)
    print("upper case: ", upper_case)
    print("lower case: ", lower_case)

if __name__ == "__main__":
    main()