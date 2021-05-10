'''
@Author: Vishal Salaskar
@Date: 2021-05-10       
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-10
@Title :  program take input and print it in upper and lower case
'''

def get_upper_lower():
    """
    Description:
    Function description : program take input and print it in upper and lower case  
    """
    try:
        data = input("Enter the string: ")
    except ValueError as e:
        print("Enter valid input",e)

    print(data.upper()) 
    print(data.lower())   

get_upper_lower()