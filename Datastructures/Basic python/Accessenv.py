'''
@Author: Vishal Salaskar
@Date: 2021-05-06
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-06
@Title : To access all the environment variables
'''
import os 

def access_env():
    """
    Description:
    Function description :To access the environment variables
    """
    environment = os.environ
    print(environment)


access_env()