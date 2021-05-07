'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title : To count the number of occurences of character in string 
'''

def count():
    """
    Description:
    Function description : To count the number of occurences of character in string 
    """
    try: 
        count = 0
        string = "Hello Welcome to Mumbai season"
        for i in string:
            if i == 'e':
                count += 1
        print(count)        
    except NameError as e:
        print(e)    

count()