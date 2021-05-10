'''
@Author: Vishal Salaskar
@Date: 2021-05-10       
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-10
@Title : program to change the occurences of  first char to $  except first char
'''

def replace():
    """
    Description:
    Function description : program to change the occurences of  first char to $  
    """
    data = "restart"
    char = data[0]
    data = data.replace(char,'$')
    data = char + data[1:]
    print(data)

replace()