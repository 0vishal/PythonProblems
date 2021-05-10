'''
@Author: Vishal Salaskar
@Date: 2021-05-10       
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-10
@Title : program to get the length of longest word in list 
'''

def get_length():
    """
    Description:
    Function description : program to get the length of longest word in list 
    """
    data = ["restart","play","wording","gambler","datastructures"]
    long = 0
    for i in data:
        string = i
        length = len(string)
        if length > long:
            long = length
    print("The length of longest one is ", long)

get_length()