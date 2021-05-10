'''
@Author: Vishal Salaskar
@Date: 2021-05-10       
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-10
@Title : program to display formatted text (width=50) as output.
'''
import textwrap

def format_string():
    """
    Description:
    Function description : program to display formatted text (width=50) as output.
    """
    str1 = "Enter the items with comma seperated: Vishal salaskar"
    print(textwrap.fill(str1,width=50))
  
format_string()