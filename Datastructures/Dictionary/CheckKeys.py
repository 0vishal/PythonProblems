'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title : To check if multiple keys exist in Dictionary
'''

def check_keys():
    '''
    Description : To check if multiple keys exist in Dictionary
    '''
    dict = {1: 2, 2: 4, 3: 5,4: 6}
    print(dict.keys() >= {1, 2})
    print(dict.keys() >= {2, 10})

check_keys()    