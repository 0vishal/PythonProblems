'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title : To list to nested dictionaries
'''

def nested_dictionaries():
    '''
    Description : To list to nested dictionaries
    '''
    num_list = [1, 2, 3 ,4 ]
    new_dict = current = {}
    for name in num_list:
        current[name] = {}
        current = current[name]
    print(new_dict)
    
nested_dictionaries()    