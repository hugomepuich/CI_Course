import unittest
from user import User

user_all_valid = User(
    "Hugo",
    "Dautremepuich",
    "abcdEFGH1234",
    "hugo@hugo.fr",
    "04-08-1998")

user_no_names = User(
    "a",
    "a",
    "abcdEFGH1234",
    "hugo@hugo.fr",
    "04-08-1998")

user_bad_pwd = User(
    "Hugo",
    "Dautremepuich",
    "abcdefghij",
    "hugo@hugo.fr",
    "04-08-1998")

user_bad_pwd_2 = User("Hugo", "Dautremepuich", "ABCDEFGHIJ", "hugo@hugo.fr", "04-08-1998")

user_bad_pwd_3 = User("Hugo", "Dautremepuich", "hfuUU23", "hugo@hugo.fr", "04-08-1998")   

user_bad_mail = User("Hugo", "Dautremepuich", "hfuUU23", "hugohugo.fr", "04-08-1998")   

user_bad_date = User(
    "Hugo",
    "Dautremepuich",
    "ABCDEFGHIJ",
    "hugo@hugo.fr",
    "0498798")

user_too_young = User("Hugo", "Dautremepuich", "hfuUU23", "hugo@hugo.fr", "04-08-2017")   

class Test_User(unittest.TestCase):
    
    def test_all_valid(self):
        self.assertTrue(user_all_valid.is_valid())
    
    # Test des noms
    def test_good_names(self):
        self.assertTrue(user_all_valid.validate_first_name())
        self.assertTrue(user_all_valid.validate_surname())
    
    def test_no_names(self):
        self.assertFalse(user_no_names.validate_first_name())
        self.assertFalse(user_no_names.validate_surname())
        
    # Test des passwords
    def test_pass_good(self):
        self.assertTrue(user_all_valid.validate_password())
        
    def test_pass_no_upper_nor_number(self):
        self.assertFalse(user_bad_pwd.validate_password())
        
    def test_pass_all_upper(self):
        self.assertFalse(user_bad_pwd_2.validate_password())
        
    def test_pass_too_short(self):
        self.assertFalse(user_bad_pwd_3.validate_password())
        
    # Test des dates
    def test_date_good(self):
        self.assertTrue(user_all_valid.validate_date_of_birth())
        
    def test_date_bad(self):
        self.assertFalse(user_bad_date.validate_date_of_birth())
        
    def test_date_too_young(self):
        self.assertFalse(user_too_young.validate_date_of_birth())
        
    # Test des emails
    def test_email_good(self):
        self.assertTrue(user_all_valid.validate_email())
        
    def test_email_bad(self):
        self.assertFalse(user_bad_mail.validate_email())
        
    # Testing the valid one
    def test_is_valid(self):
        self.assertTrue(user_all_valid.is_valid())
    
    # All other users are not valid
    def test_is_not_valid(self):
        self.assertFalse(user_no_names.is_valid())
        self.assertFalse(user_bad_pwd.is_valid())
        self.assertFalse(user_bad_pwd_2.is_valid())
        self.assertFalse(user_bad_pwd_3.is_valid())
        self.assertFalse(user_bad_date.is_valid())
        self.assertFalse(user_too_young.is_valid())
        self.assertFalse(user_bad_mail.is_valid())
        