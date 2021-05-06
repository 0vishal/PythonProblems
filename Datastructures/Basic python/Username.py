'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To take input username and give output in reverse order
'''

try:
    username = input("Enter the full username ")
except ValueError as e:
    print("Enter correct input", e)    

def reverse_username():
    """
    Description:
    Function description : To get username in reverse order
    """
    try:    
        split_name= username.split(' ')    
        print(split_name[1],split_name[0])
    except IndexError as e:
        print("Enter correct input", e)    

reverse_username()        

