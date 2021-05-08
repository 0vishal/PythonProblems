'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title : To convert string to dictionary
'''

def convert():
    '''
    Description : To convert string to dictionary with the count of characters 
    '''
    string = "welcome"
    dict = {}
    for i in string:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1    
    print(dict)
   
convert()    