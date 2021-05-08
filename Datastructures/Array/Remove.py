'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title :  To  remove the value from array
'''

from array import *

def remove():
    """
    Description:
    Function description : To  remove the value from array
    """   
    data = [1,2,3,4,5,7,2,4,6,7,2,7]
    number = 7
    print(data.count(number))
    data2 = array('i',[1,2,3,4,5,7,2,4,6,7,2,7])
    data2.remove(3)
    print(data2)

remove()    