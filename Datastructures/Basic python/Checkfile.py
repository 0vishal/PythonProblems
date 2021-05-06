'''
@Author: Vishal Salaskar
@Date: 2021-05-06
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-06
@Title : To check if file exist or not
'''

def check():
    """
    Description:
    Function description : To find if file exists or not
    """
    try:
        f = open("Vishal.txt")
        print(f.read())
    except Exception as e:
        print(e)

check()