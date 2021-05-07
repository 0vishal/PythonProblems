'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title : To clear the screen of terminal  
'''
import time 
import os
    

def clear_screen(): 
    """
    Description:
    Function description : To clear the screen of terminal 
    """   
    os.system('ls')
    time.sleep(2)
    os.system('clear')
    

clear_screen()