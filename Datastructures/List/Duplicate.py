'''
@Author: Vishal Salaskar
@Date: 2021-05-09
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : To program to remove the duplicate from list
'''

def remove_duplicate():
    """
    Description:
    Function description : To program to remove the duplicate from list of lists
    """
    data = [[1, 2], [4], [5, 6, 2], [1, 2], [3], [4]]
    newdata = []
    for element in data:
        if element not in newdata:
            newdata.append(element)
    data = newdata
    print(data)
   
remove_duplicate()    