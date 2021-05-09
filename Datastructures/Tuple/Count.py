'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : program to count the number of repeated value in tuple  
'''

def count_value():
    """
    Description:
    Function description : program to count the number of repeated value in tuple 
    """
    data = (1,2,3,4,5,3,2,4,5,2)
    count = data.count(2)
    print("The number 2 is repeated ", count, "Times")
   
count_value()