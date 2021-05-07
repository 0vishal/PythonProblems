'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title : To take and print the size of object
'''
import sys


def limit():
    """
    Description:
    Function description : To print and take the size of object
    """
    try: 
        print(sys.getrecursionlimit())
    except NameError as e:
        print(e)    

limit()