'''
@Author: Vishal Salaskar
@Date: 2021-05-10       
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-10
@Title : program to replace string values end with ing and ly according to given condition
'''

def replace():
    """
    Description:
    Function description : program to replace string values end with ing and ly according to given condition
    """
    data = "rising"
    minlength = 3
    if len(data) > minlength:
        if data.endswith("ing"):
            data = data.replace("ing","ly")
        else:
            data = data.replace(data[-4:],"ing")
    print(data)            

replace()