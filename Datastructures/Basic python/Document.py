'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To print the document of the built in python functions
'''

a = 5
b = 3

def functions_doc():
    """
    Description:
    Function description : To get documentation of the function 
    """
    print(min(a,b))
    print(min.__doc__)

functions_doc()