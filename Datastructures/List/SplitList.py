'''
@Author: Vishal Salaskar
@Date: 2021-05-09
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : To program to split a list on character of word
'''
from itertools import groupby
from operator import itemgetter

def common():
    """
    Description:
    Function description : To program to split a list on character of word
    """
    data = ['About', 'Absolutely', 'After', 'Aint', 'Alabama', 'AlabamaBill', 'All', 'Also', 'Amos', 'And', 'Anyhow', 'Are', 'As', 'At', 'Aunt', 'Aw', 'Bedlam', 'Behind', 'Besides', 'Biblical', 'Bill', 'Billgone']
    for letter, words in groupby(sorted(data), key=itemgetter(0)):
        print(letter)
        for word in words:
            print(word)
common()   

