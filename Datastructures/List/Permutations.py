'''
@Author: Vishal Salaskar
@Date: 2021-05-09
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : To program to generate permutations from list
'''
import itertools

def get_permutations():
    """
    Description:
    Function description : To program to generate permutations from list
    """
    newlist = list(itertools.permutations([1,2,3,4,5]))
    print(newlist)
  

get_permutations()   

