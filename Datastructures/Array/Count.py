'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title :  To  print the number of occurences in array 
'''
from array import *

def count():
    """
    Description:
    Function description : To  print the number of occurences in array 
    """   
    data = [1,2,3,4,5,7,2,4,6,7,2,7]
    number = 7
    print(data.count(number))
    data2 = array('i',[1,2,3,4,5,7,2,4,6,7,2,7])
    print(data2.count(number))
    

count()    