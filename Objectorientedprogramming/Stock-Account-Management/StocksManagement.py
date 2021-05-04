'''
@Author: Vishal Salaskar
@Date: 2021-04-05 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-04-05
@Title : To add load calculate and update the stock portfolio
'''

import json
class StocksManagement:

    def __init__(self):
        pass

    def listOfStocks(self):
        self.totalcost={}
        try:
            with open("F:\Python\Object oriented programming\Stock-Account-Management\stocks.json",'r') as jsonfile:
                self.data = json.load(jsonfile)
                return self.data
        except Exception as e : 
            print(e) 

    def calculate(self):
        """
        Description:
        A function to calculate the total stocks value 
        Parameter:
        None
        """ 
        data=self.listOfStocks()

        for stock_name in data:
                self.total= float(data[stock_name].get("Numberofshares")) * float(data[stock_name].get("shareprice"))
                self.totalcost[stock_name]=self.total
        print(self.totalcost)
        self.uploadData(self.totalcost)

    def uploadData(self,totalcost):
        try:
            with open("F:\Python\Object oriented programming\Stock-Account-Management\stock_portfolio.json",'w') as jsonfile:
                json.dump(totalcost, jsonfile,indent=4)
        except Exception as e:
            print(e)    

    
if __name__ == "__main__":
    stocks = StocksManagement()
    stocks.listOfStocks()
    stocks.calculate()