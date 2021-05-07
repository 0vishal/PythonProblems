'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title : To take input command line arguments passed to script
'''
import sys


def print_arguments():
    """
    Description:
    Function description : To print the arguments values to the script
    """
    try: 
        print("This is the name/path of the script:", sys.argv[0])
        print("Number of arguments:",len(sys.argv))
        print("Argument List:",str(sys.argv))
    except NameError as e:
        print(e)    

print_arguments()