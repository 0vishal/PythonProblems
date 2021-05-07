'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title : To print the recursion limit
'''
import sys


def limit():
    """
    Description:
    Function description : To print the recursion limit
    """
    try: 
        print(sys.getrecursionlimit())
    except NameError as e:
        print(e)    

limit()