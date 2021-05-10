'''
@Author: Vishal Salaskar
@Date: 2021-05-09
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : To program to remove from list
'''

def remove():
    """
    Description:
    Function description : To program to remove from list
    """
    data = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    
    data = [x for (i,x) in enumerate(data) if i not in (0,4,5)]
    print(data)
  


remove()   

