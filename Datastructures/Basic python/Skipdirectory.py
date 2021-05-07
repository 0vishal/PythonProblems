'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title :  To find file and skip directory  
'''
import os

def skip_directory():
    """
    Description:
    Function description : To find file and skip directory  
    """   
    for root, dirs, files in os.walk("."):
        for filename in files:
            print(filename)
   
skip_directory()    