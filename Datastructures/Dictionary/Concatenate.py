'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title : To concatenate dictionary to create one 
'''

def add():
    '''
    Description : To concatenate dictionary to create one 
    '''
    dict1 = { 1: 2, 2: 4}
    dict2 = { 3: 6, 4: 3}
    dict3 = { 5: 9, 6: 1}
    dict4 = {}
    for i in (dict1,dict2,dict3):
        dict4.update(i)
    print(dict4)
    
add()    