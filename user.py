from todolist import ToDoList

class User:
    def __init__(self, 
                    first_name: str,
                    surname: str,
                    password: str,
                    email : str,
                    date_of_birth: str
                 ):
        self.first_name = first_name
        self.surname = surname
        self.password = password
        self.email = email
        self.date_of_birth = date_of_birth
        self.to_do_list = ToDoList()
        self.to_do_list.owner = self
        self.mails = []
    
    # email is valid
    def validate_email(self):
        return '@' in self.email and '.' in self.email and len(self.email) > 5
    
    # 40 > Password length > 8  
    def validate_password(self):
        len_validated = len(self.password) >= 8 and len(self.password) <= 40
        has_up_and_low = self.password.lower() != self.password and self.password.upper() != self.password  
        has_one_number = False
        chars = 0
        for i in range(len(self.password)):
            if self.password[i].isdigit():
                has_one_number = True
                continue
            if self.password[i].isalpha():
                chars += 1
                continue
            if has_one_number and chars >= 2:
                break
        
        return len_validated and has_up_and_low and has_one_number and chars >= 2
    
    # First name exists
    def validate_first_name(self):
        return self.first_name is not None and len(self.first_name) > 2
    
    # Surname exists
    def validate_surname(self):
        return self.surname is not None and len(self.surname) > 2
    
    def validate_date_of_birth(self):
        import datetime
        try:
            date = datetime.datetime.strptime(self.date_of_birth, '%d-%m-%Y')
            now = datetime.datetime.now()
            delta = now - date
            return (delta.days / 365 >= 13)
        except ValueError:
            return False
    
    # User is valid
    def is_valid(self):
        return self.validate_date_of_birth() and self.validate_email() and self.validate_first_name() and self.validate_surname() and self.validate_password()
        