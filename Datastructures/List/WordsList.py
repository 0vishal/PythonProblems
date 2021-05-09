'''
@Author: Vishal Salaskar
@Date: 2021-05-09
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title : program the list of words with specified words length
'''

def get_wordslist():
    """
    Description:
    Function description : To program the list of words with specified words length
    """
    string = "This is a new channel of Panda Xpress on youtube"
    minlength = 3 
    newlist = [] 
    words = string.split(" ")
    for i in words:
        if len(i) > minlength:
            newlist.append(i)
    print(newlist)        
     
get_wordslist()