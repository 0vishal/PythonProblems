'''
@Author: Vishal Salaskar
@Date: 2021-04-05 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-04-05
@Title : To add load calculate and update the inventory of wheat rice pulses 
'''
import json
import math

class InventoryManagement:

    def __init__(self):
        pass


    def loadData(self):
         """
        Description:
        A function to load the data from json file
        Parameter:
        None
        """  
 
        self.totalcost={}
        try:
            with open("F:\Python\Object oriented programming\JsonInventoryDataManagement\Inventory.json",'r') as jsonfile:
                data =  json.load(jsonfile) 
                jsonfile.close()   
                return data
        except Exception as e : 
            print(e)


    def calculate(self):
        """
        Description:
        A function to calculate the inventory value
        Parameter:
        None
        """  
        data=self.loadData()
        for item_type in data:
            for item in data.get(item_type): 
                self.total= float(data[item_type][item].get("price")) * float(data[item_type][item].get("weight"))
                self.totalcost[item]=self.total
        print(self.totalcost)
        self.uploadData(self.totalcost)

    def uploadData(self,totalcost):
        """
        Description:
        A function to update data to file
        Parameter:
        None
        """  
        try:
            with open("F:\Python\Object oriented programming\JsonInventoryDataManagement\Inventorysummary.json",'w') as jsonfile:
                json.dump(totalcost, jsonfile,indent=4)
        except Exception as e:
            print(e)        


if __name__ == "__main__":

    inventory = InventoryManagement()
    inventory.calculate()