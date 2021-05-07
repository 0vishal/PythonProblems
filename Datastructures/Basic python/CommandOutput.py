'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title :  To get command output on terminal 
'''
import subprocess    

def command_output(): 
    """
    Description:
    Function description : To get command output on terminal
    """   
    output = subprocess.check_output("ls",universal_newlines=True)
    print("ls command output ")
    print(output)

command_output()