'''
@Author: Vishal Salaskar
@Date: 2021-05-08
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-08
@Title : To get dictionary in table format
'''

def get_table():
    '''
    Description : To get dictionary in table format
    '''
    dict = {1: ["Vishal",24,"Mumbai"], 2: ["Sarvesg",18,"Pune"], 3: ["Rahul",26,"Navimumbai"]}
    print("{:<10} {:<10} {:<10}".format('Name','Age','City'))
    for key, value in dict.items():
        name, age, city = value
        print("{:<10} {:<10} {:<10}".format(name,age,city))
   
get_table()    