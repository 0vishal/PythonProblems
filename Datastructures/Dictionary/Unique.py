'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title : To get unique values in dictionary
'''

def unique():
    '''
    Description : To get unique values in dictionary using set 
    '''
    dict = { 1: 2, 2: 4, 3: 6, 4: 3, 5: 9, 6: 1, 7: 3, 8: 4, 9: 2, 10: 6 }
    print(dict)
    sort = sorted(dict.values())
    print(set(sort))
    
unique()
