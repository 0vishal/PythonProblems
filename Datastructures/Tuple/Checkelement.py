'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : program to check if element exists or not 
'''

def check():
    """
    Description:
    Function description : program to check if element exists or not 
    """
    data = (1,2,3,4,5,3,2,4,5,2)
    check_value = 2
    for i in data:
        if check_value == i:
            result = True
    print(result)        
   
check()