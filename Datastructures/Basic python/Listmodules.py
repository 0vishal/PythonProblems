'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title : To print all the built in modules
'''


def print_modules():
    """
    Description:
    Function description : To print all the builtin modules 
    """
    try: 
       print(dir("__builtin__"))
    except NameError as e:
        print(e)    

print_modules()