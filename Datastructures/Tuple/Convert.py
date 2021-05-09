'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title :  program to convert list to tuple
'''

def convert():
    """
    Description:
    Function description : program to convert list to tuple 
    """
    data = ["apple", "banana", "cherry"]
    print(type(data))
    data2 = tuple(data)
    print(type(data2))

convert()