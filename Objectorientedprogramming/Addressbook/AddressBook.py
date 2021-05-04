'''
@Author: Vishal Salaskar
@Date: 2021-04-05 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-04-05
@Title : To add update delete person contact from addressbook
'''

class AddressBook:

    def __init__(self):
        pass


    def loadData(self):
        try: 
            self.data=json.load(open(r"F:\Python\Objectorientedprogramming\Addressbook\addressbook.json"))        
        except Exception as e :
            print("Error Unable to open the file : ",e)

     def selectOption(self):
        """
        Description:
        A function to choose option to add update delete 
        Parameter:
        None
        """  
        
        option = int(input("Enter option \n1:Add contact\n2:Update contact\n3:Delete contact\n\n4:Quit \n:"))
                
        if option == 1:
            addAddress()
        elif option == 2:
            updateAddress()
        elif option == 3:
            deleteAddress()
        else:
            print("Select Valid option")
            self.selectOption()          


    def deleteAddress(self): 
        """
        Description:
        A function to delete contact in addressbook 
        Parameter:
        None
        """         

        
        try:
            for person in self.data["addressbook"]["first_name"]:
                    print(person)
            person=int(input("Select person name"))
            del(self.data["addressbook"]["first_name"])            
        except Exception as e:
            print(e)
            self.deleteAddress()


    def updateAddress(self):
        """
        Description:
        A function to update contact in addressbook 
        Parameter:
        None
        """  

        try:
            for person in self.data["addressbook"]["first_name"]:
                    print(person)
            person=int(input("Select person name"))

            selected_person=input("Enter Person name : ")
            person_details=self.data["addressbook"].get(selected_person)

            for detail_key,detail_value in person_details.items():
                print(f" {detail_key} : {detail_value}")

            property=input("Enter person property you want to update : ")  

            value=input("Enter the value you want to update : ")  
            self.data["AddressBook"]["first_name"][property]=value

            self.uploadData()

    def addAddress():
        """
        Description:
        A function to add contact in addressbook 
        Parameter:
        None
        """  

        try:
            new_fname=str(input("enter first name: "))
            new_lname=str(input("enter last name: "))
            new_address=str(input("enter address: "))
            new_city=str(input("enter city: "))
            new_state=str(input("enter state: "))
            new_zip=str(input("enter zip: "))
            new_phone_number=str(input("enter phone number: "))
        except Exception as e:
            print("Value cannot be empty", e)        
        person_details={ 
                    "first_name": new_fname,
                    "last_name": new_lname,
                    "address": new_address,
                    "city": new_city,
                    "state": new_state,
                    "zip": new_zip,
                    "phone_number": new_phone_number
        }
        self.data["AddressBook"]=person_details

        self.uploadData()




    def uploadData(self):
        """
        Description:
        A function to update data to json file 
        Parameter:
        None
        """  
        try:
            with open(r"F:\Python\Objectorientedprogramming\Addressbook\addressbook.json",'w') as address_book:
                json.dump(self.data,address_book,indent=7)
        
        except Exception as e:
            print(e)




if __name__ == "__main__":
    book = AddressBook()
    address_book.loadData()
    address_book.selectOption()