'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title :  program to use frozen sets 
'''

def create():
    """
    Description:
    Function description : program to use frozen sets  
    """
    data = {}
    list = [1,2,3,4,5]
    dict = {'name': 'Vishal','Age': 24}
    frozen1 = frozenset(dict)
    frozen2 = frozenset(list)
    print(frozen1)
    print(frozen2)
    print(frozen3)

create()