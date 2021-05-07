'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title :  To check a variable is defined or not 
'''
def variable_define():
    """
    Description:
    Function description : To check a variable is defined or not  
    """   
    try:
        x 
    except NameError:
        print("Variable is not defined")
    else:
        print("Variable is defined.")

variable_define()    