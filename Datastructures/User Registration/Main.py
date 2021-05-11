'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title :  program to create user registration form with regex and logger
'''
import re
import logging

logging.basicConfig(filename='logging.log',level=logging.INFO,format='%(levelname)s : %(asctime)s: %(message)s')

class main():
    """
    Description:
    Function description : program to create user registration form with regex and logger
    """
    def validate_username(self,user_name):
            regex_username = "^[A-Z]{1}[a-z]{2,}$"
            pattern1 = re.compile(regex_username)
            match1 = re.search(pattern1, user_name)
            if match1:
                return "valid username"
            else:    
                return "invalid username"
                
        
    def validate_password(self,password):
            regex_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
            pattern2 = re.compile(regex_password)
            match2 = re.search(pattern2, password)
            if match2:
                return "valid password"
            else:    
                return "invalid password"


    def validate_email(self,email):
            regex_email = "[A-za-z0-9.-]+@[a-zA-z]+\.com"
            pattern3 = re.compile(regex_email)
            match3 = re.search(pattern3, email)
            if match3:
                    return "valid emailid"
            else:    
                    return "Invalid emailid"

    
if __name__ == '__main__':
    try:
        user_name = input("Enter the first name:  ")
        logging.info("username successfully created {}".format(user_name))
    except ValueError as error:
        print(error)
        print("Wrong input") 
    user_name_validation = main().validate_username(user_name)    
    print(user_name_validation)

    try:    
        print("\n")
        password = input("Enter the password:  ")
        logging.info("password successfully created for {}".format(user_name))
    except ValueError as error:
        print(error)
        print("Wrong input")
    password_validation = main().validate_password(password)  
    print(password_validation)

    try: 
        print("\n")   
        email = input("Enter the email id:  ")
        logging.info("Email id successfully created for {}".format(user_name))
    except ValueError as error:
        print(error)
        print("Wrong input")  
    email_validation = main().validate_email(email)    
    print(email_validation)
        
    print("\n")
    print("User Details : ", user_name, password, email)

 