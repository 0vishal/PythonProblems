'''
@Author: Vishal Salaskar
@Date: 2021-02-29 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-02-29 
@Title : To take input integers and sort 
'''
def sort():
      """
    Description:
    Function description : To get the file time of creation and modification
    """
    try:
        integer = []
        for i in range(0,3):
            integers = int(input("Enter  integers \n"))
            integer.append(integers)
        sort = sorted(integer)    
        print(sort)
    except ValueError as e:
        print("Enter correct input", e)    

sort()