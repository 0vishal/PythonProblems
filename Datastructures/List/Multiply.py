'''
@Author: Vishal Salaskar
@Date: 2021-05-09
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : program to multiplies all the items in a list.

'''

def multiply():
    """
    Description:
    Function description : program to multiplies all the items in a list.
    """
    list = [1,2,3,4,5,5,6]
    multiplies = 1
    for i in list:
        multiplies = multiplies * i
    print(multiplies)    


multiply()