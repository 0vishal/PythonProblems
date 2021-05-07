'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title : To get the current system time  
'''
import datetime 
    

def time(): 
    """
    Description:
    Function description : To get the system time
    """   
    current_time = datetime.datetime.now() 
    print (current_time) 

time()