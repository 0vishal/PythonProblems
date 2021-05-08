'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title : To count the values from dictionaries
'''

def get_table():
    '''
    Description : To count the specified values from dictionaries
    '''
    count = 0
    data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
    False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
    for i in range(0,len(data)):
        if data[i]['success'] == True:
                count += 1
    print(count)
   
get_table()    