'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title : To sort a dictionary
'''

def sort():
    '''
    Description : To sort a dictionary 
    '''
    dict = { 1: 2, 2: 4, 3: 6, 4: 3, 5: 9, 6: 1}
    print(dict)
    print(sorted(dict.values(),reverse=True))
    sort= sorted(dict.values())
    print(sort)


sort()    