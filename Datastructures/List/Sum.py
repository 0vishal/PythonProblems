'''
@Author: Vishal Salaskar
@Date: 2021-05-09
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : To program to sum all the items in a list.
'''

def sum():
    """
    Description:
    Function description : To program to sum all the items in a list.
    """
    list = [1,2,3,4,5,5,6]
    sum = 0 
    for i in list:
        sum += i
    print(sum)    


sum()