'''
@Author: Vishal Salaskar
@Date: 2021-05-07 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-07 
@Title :  To get file properties using function
'''
import os    

def file_property(): 
    """
    Description:
    Function description : To get file properties to read and write and append file 
    """   

    file = open("Test.txt","r")
    content = file.read()
    file.close()

    file = open("Test.txt","w")
    file.write("This is a new line ")
    file.close()


    file = open("Test.txt","a")
    file.write("The is the append content") 
    file.close()

 
file_property()