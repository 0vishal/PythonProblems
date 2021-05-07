'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title : To get the hostname
'''
import socket
    

def get_hostname(): 
    """
    Description:
    Function description : To get the hostname of the system
    """   
    host_name = socket.gethostname()
    print("Host name ", host_name)
    

get_hostname()