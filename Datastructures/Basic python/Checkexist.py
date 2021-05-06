'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To Check if value exist in group of values
'''

def check_value():
    values = [1,3,4,5,6]
    value =  int(input("Enter the value to check if exists: "))
    check = any(value for value in values)
    print(check)

check_value()    