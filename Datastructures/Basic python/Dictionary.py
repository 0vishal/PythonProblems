'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title :  To get key value of dictionary  
'''
import os

def get_keyvalue():
    """
    Description:
    Function description : To get key value of dictionary  
    """
    dict = {'color' : 'green'}
    (key, value), = dict.items()
    print(key)
    print(value)

get_keyvalue()    