'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title : To add a key in dictionary
'''

def add():
    '''
    Description : To add key to dictionary
    '''
    dict = { 1: 2, 2: 4, 3: 6, 4: 3, 5: 9, 6: 1}
    print(dict)
    dict.update({7: 10})
    print(dict)

add()    