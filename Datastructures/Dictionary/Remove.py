'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title : To remove a key from dictionary
'''

def remove():
    '''
    Description : To remove a key from dictionary
    '''
    dict = { 1: 2, 2: 4, 3: 6, 4: 3, 5: 9, 6: 1}
    print(dict)
    del dict[1]
    print(dict)

remove()    