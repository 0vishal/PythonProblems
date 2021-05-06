'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To print the calender of given month 
# Program to display calendar of the given month and year
'''
import calendar
  
def display():
    """
    Description:
    Function description :To access the environment variables
    """
    try:
        yy = int(input("Enter year: "))
        mm = int(input("Enter month: "))
    except Exception as e:
        print(e)    
    print(calendar.month(yy,mm))

display()    