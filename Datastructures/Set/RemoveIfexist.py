'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title :  program to remove from set
'''

def add():
    """
    Description:
    Function description : program to remove from set  
    """
    data = {}
    data = {1,2,3,4,5,6}
    if 1 in data:
        data.remove(1)
    print(data)    

add()