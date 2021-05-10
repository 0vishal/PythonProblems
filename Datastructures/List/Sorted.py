'''
@Author: Vishal Salaskar
@Date: 2021-05-09
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : program get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
'''

def sort_tuple():
    """
    Description:
    Function description : To program get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.
    """
    data = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    data.sort(key= lambda x : x[-1])
    print(data)

     
sort_tuple()

