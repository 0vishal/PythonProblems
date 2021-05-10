'''
@Author: Vishal Salaskar
@Date: 2021-05-10       
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-10
@Title : program to get last part of string after specified character
'''

def split_string():
    """
    Description:
    Function description : program to get last part of string after specified character
    """
    str1 = "Enter the items with comma seperated: Vishal salaskar"
    split = str1.rsplit(":",1)[1]
    print(split)

split_string()