'''
@Author: Vishal Salaskar
@Date: 2021-05-09
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : To program to find common between two list
'''

def find_common():
    """
    Description:
    Function description : To program to find common between two list
    """
    list1 = [1,2,3,4,5,5,2,3,6]
    list2 = [2,3,4,5,6,4]
    for x in list1:
        for y in list2:
            if x == y :
                common = True
    print(common)
   
find_common()