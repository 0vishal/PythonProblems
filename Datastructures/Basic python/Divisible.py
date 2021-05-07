'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title :  To get divisible by 15
'''
import os    

def divisible(): 
    """
    Description:
    Function description : To get numbers divisible by 15
    """   
    number = [45, 55, 60, 37, 100, 105, 220]
    result = list(filter(lambda x: (x % 15 == 0), number))
    print("Numbers divisible by 15 are",result)

 
divisible()