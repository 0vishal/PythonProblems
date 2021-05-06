'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To take input sequence of number and give it in tuple and list
'''

def convert():
    """
    Description:
    Function description : To get input in list and tuple
    """
    try:
        numbers = [int(i) for i in input("Enter the number with comma seperately\n").split(', ')] 
        print(f"{numbers}")
        print(tuple(numbers))
    except ValueError as e:
        print(e)

convert()