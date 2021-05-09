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
    Function description : To program to remove the duplicate from list
    """
    list = [1,2,3,4,5,5,2,3,6]
    newlist = []
    for i in list:
        if i not in newlist:
            newlist.append(i)
    print(newlist)
   
remove_duplicate()