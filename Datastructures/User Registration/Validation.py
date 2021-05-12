import re


def validate_username(user_name):
        regex_username = "^[A-Z]{1}[a-z]{2,}$"
        pattern1 = re.compile(regex_username)
        match1 = re.search(pattern1, user_name)
        if match1:
            return "valid username"
        else:    
            return "invalid username"
                
        
def validate_password(password):
        regex_password = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pattern2 = re.compile(regex_password)
        match2 = re.search(pattern2, password)
        if match2:
            return "valid password"
        else:    
            return "invalid password"

def validate_email(email):
        regex_email = "[A-za-z0-9.-]+@[a-zA-z]+\.(com,edu,in)"
        pattern3 = re.compile(regex_email)
        match3 = re.search(pattern3, email)
        if match3:
                return "valid emailid"
        else:    
                return "Invalid emailid"
