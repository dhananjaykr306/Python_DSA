'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program to print the calendar of a given month and year using the 'calendar' module.
'''

import calendar

def print_calendar(year, month):
    """
        Description :
            This function prints the calendar of a given month and year.
        Parameters :
            year : The year for which the calendar is to be printed.
            month : The month for which the calendar is to be printed.
        Return :
            None
    """

    print(calendar.month(year, month))

def main():
    year = int(input("Enter year: "))
    month = int(input("Enter month (1-12): "))
    
    print_calendar(year, month)

if __name__=="__main__":
    main()