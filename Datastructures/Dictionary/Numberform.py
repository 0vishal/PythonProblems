'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title : To generate a number form of dictionary
'''

def number_form():
    '''
    Description :  To generate a number form of dictionary
    '''
    dict = {}
    try:
        number = int(input("Enter a number: "))
    except ValueError: 
        print("Enter valid input")    
    try:    
        for i in range(1,number):
            dict.update({i: i*i})
        print(dict)
    except UnboundLocalError as e:
        print("Enter valid input", e)
        
number_form()    