'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title :  program to get the symmetric difference of sets
'''

def symmetric():
    """
    Description:
    Function description : program to get the symmetric difference of sets
    """
    data1 = {1,2,3,4,5,6}
    data2 = {4,5,6,7,8,9}
    data3 = data1 ^ data2
    print(data3)

symmetric()