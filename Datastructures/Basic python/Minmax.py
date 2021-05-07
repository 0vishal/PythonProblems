'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title :  To get minimum and maximum of sequence of numbers 
'''

def get_minmax():
    """
    Description:
    Function description : To get minimum and maximum of sequence of numbers 
    """
    data = [1,2,3,4,5]
    min = data[0]
    max = data[0]
    for num in data:
        if num > min:
            min = num
        elif num < max:
            max = num
    print(min)
    print(max)
        
get_minmax() 