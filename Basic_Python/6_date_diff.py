'''
    @Author: Dhananjay Kumar
    @Date: 07-10-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 07-10-2024
    @Title : Python program to calculate the number of days between two dates.
'''

from datetime import date

def calculate_days(date1, date2):
    """
        Description :
            This function calculates the number of days between two dates.
        Parameters :
            date1 : The first date (year, month, day)
            date2 : The second date (year, month, day)
        Return :
            The number of days between the two dates
    """
    delta = abs(date2 - date1)
    return delta.days

def main():
    year1 = int(input("Enter the year of the first date: "))
    month1 = int(input("Enter the month of the first date: "))
    day1 = int(input("Enter the day of the first date: "))
    
    year2 = int(input("Enter the year of the second date: "))
    month2 = int(input("Enter the month of the second date: "))
    day2 = int(input("Enter the day of the second date: "))
    
    date1 = date(year1, month1, day1)
    date2 = date(year2, month2, day2)
    
    days_between = calculate_days(date1, date2)
    
    print(f"Number of days between {date1} and {date2} is: {days_between} days")


if __name__ == "__main__":
    main()