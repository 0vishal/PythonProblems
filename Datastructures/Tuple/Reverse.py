'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : program to reverse a tuple
'''

def reverse_tuple():
    """
    Description:
    Function description :  program to reverse a tuple
    """
    data = (1,2,3,4,5)
    data2 = reversed(data)
    print(tuple(data2))        
   
reverse_tuple()