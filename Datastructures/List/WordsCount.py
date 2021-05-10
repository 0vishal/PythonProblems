'''
@Author: Vishal Salaskar
@Date: 2021-05-09
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : program the list of words with specified words length and  and first and last character is same
'''

def get_wordscount():
    """
    Description:
    Function description : To program the list of words with specified words length  and first and last character is same
    """
    words = ["aba","jaba","tany","osho"]
    minlength = 3 
    count = 0
    for word in words:
        if len(word) > minlength and word[1] == word[-1]:
            count += 1
    print(count)        
     
get_wordscount()