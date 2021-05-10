'''
@Author: Vishal Salaskar
@Date: 2021-05-10       
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-10
@Title : program to print unique words in sorted form 
'''

def sort_unique():
    """
    Description:
    Function description : program to print unique words in sorted form 
    """
    try:
        words = input("Enter the items with comma seperated")
        word = []
        for i in words:
            word = words.split(",")
        print(",".join(sorted(list(set(word)))))
    except ValueError as e:
        print("Enter correctly", e)        
    
sort_unique()