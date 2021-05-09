'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : program to remove item from tuple 
'''

def remove_item():
    """
    Description:
    Function description : program to remove item from tuple
    """
    data = [1,2,3,4,5]
    data2 = list(data)
    data2.remove(2)
    newtuple = tuple(data2)
    print(newtuple)        
   
remove_item()