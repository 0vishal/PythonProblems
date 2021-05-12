'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title :  program to create user registration form with regex and logger
'''

import log  
import Validation

def main():
    try:
        user_name = input("Enter the first name:  ")
        log.logger("username successfully created ",user_name)
    except ValueError as error:
        print(error)
        print("Wrong input") 
    user_name_validation = Validation.validate_username(user_name)    
    print(user_name_validation)

    try:    
        print("\n")
        password = input("Enter the password:  ")
        log.logger("password successfully created",user_name)
    except ValueError as error:
        print(error)
        print("Wrong input")
    password_validation = Validation.validate_password(password)  
    print(password_validation)

    try: 
        print("\n")   
        email = input("Enter the email id:  ")
        log.logger("Email id successfully created  ",user_name)
    except ValueError as error:
        print(error)
        print("Wrong input")  
    email_validation = Validation.validate_email(email)    
    print(email_validation)
        
    print("\n")
    print("User Details : ", user_name, password, email)

main()


