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
    try:
        username = getpass.getuser()
        print(username)
    except Exception as e:
        print('Error Occured : ', e)

get_username()


