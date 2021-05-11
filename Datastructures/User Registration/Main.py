'''
@Author: Vishal Salaskar
@Date: 2021-05-09 
@Last Modified by: Vishal Salaskar
@Last Modified time: 2021-05-09 
@Title :  program to create user registration form with regex and logger
'''
import re

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
        print(main().validate_username(user_name))
        
        print("\n")
        password = input("Enter the password:  ")
        print(main().validate_password(password))
        
        print("\n")
        email = input("Enter the email id:  ")
        print(main().validate_email(email))
        
        print("\n")
        print("User Details : ", user_name, password, email)

    except ValueError as e:
        print("Enter correct input",e)
 