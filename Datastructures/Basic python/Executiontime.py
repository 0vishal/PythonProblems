'''
@Author: Vishal Salaskar
@Date: 2021-05-06
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-06
@Title : To calculate the time for a method
'''
import time
import calendar
  
t0 = time.time()
def execution_time():
    """
    Description:
    Function description :To get execution time for method
    """
    try:
        yy = int(input("Enter year: "))
        mm = int(input("Enter month: "))
    except Exception as e:
        print(e)    
    print(calendar.month(yy,mm))

execution_time()
t1 = time.time()
total_time = t1 - t0

print("Time in cpu seconds: ", t1)