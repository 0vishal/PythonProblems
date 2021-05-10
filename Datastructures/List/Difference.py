'''
@Author: Vishal Salaskar
@Date: 2021-05-09
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : To program to find difference of set
'''
import itertools

def get_difference():
    """
    Description:
    Function description : To program to find difference of set
    """
    data1 = [1,2,3,4,5]
    data2 = [4,5,6,7]
    newlist = list(set(data1) - set(data2))
    print(newlist)
  

get_difference()   

