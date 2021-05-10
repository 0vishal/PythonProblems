'''
@Author: Vishal Salaskar
@Date: 2021-05-10       
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-10
@Title :  program to calculate the character frequency of string 
'''

def get_length():
    """
    Description:
    Function description : program to calculate the character frequency of string  
    """
    data = "Welcome"
    frequency = {}
    print(len(data))
    for i in data: 
        if i in frequency:
            frequency[i] += 1
        else:
            frequency[i] = 1
    print(frequency) 

get_length()