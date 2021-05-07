'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title : To take and print the size of object
'''
import sys


def object_size():
    """
    Description:
    Function description : To print and take the size of object
    """
    try: 
        x = 2
        print(sys.getsizeof(x))
        print(sys.getrecursionlimit())
    except NameError as e:
        print(e)    

object_size()