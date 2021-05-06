'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To print the set which exist in 1 and not in 2
'''

def color_difference():
    """
    Description:
    Function description : To find out the difference of set 1 not in set 2 
    """
    color_list1 = set(['White','Black','Red'])
    color_list2 = set(['Red','Green'])
    difference = color_list1.difference(color_list2)
    print(difference)

color_difference()


