'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title :  program to remove from set
'''

def remove():
    """
    Description:
    Function description : program to remove from set  
    """
    data = {}
    data = {1,2,3,4,5,6}
    data.remove(6)
    for i in data:
        print(i)

remove()