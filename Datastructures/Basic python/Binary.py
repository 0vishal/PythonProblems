'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title :  To get binary with zeros 
'''
import os

def get_binary():
    """
    Description:
    Function description : To get binary with zeros  
    """
    num = 5
    binary = format(num, "010b")
    print(binary)

get_binary()    