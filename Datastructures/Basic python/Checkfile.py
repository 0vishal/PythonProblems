'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To print the calender of given month 
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