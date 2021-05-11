import unittest
import sys
import Main


class Test_valid_name(unittest.TestCase):
    """
    Description:
        This class define for test username email id and password 
    """

    def test_validusername(self):
        """
        Description:
            This method define for test all case of valid_username method
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(Main.main().validate_username("Vishal"),"valid username")

    def test_validpassword(self):
        """
        Description:
            This method define for test all case of valid_password method
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(Main.main().validate_password("Vishal@123"),"valid password")

    def test_validemailid(self): 
        """
        Description:
            This method define for test all case of valid_email method
        Parameter:
            None
        Return:
            None
        """
        self.assertEqual(Main.main().validate_email("vishal@gmail.com"),"valid emailid")




if __name__ == '__main__':
    unittest.main()
