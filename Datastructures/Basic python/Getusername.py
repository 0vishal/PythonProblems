'''
@Author: Vishal Salaskar
@Date: 2021-05-06
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-06
@Title : To get the current username
'''
import getpass

def get_username():
    """
    Description:
    Function description :To get the current username 
    """
    username = getpass.getuser()
    print(username)

get_username()


