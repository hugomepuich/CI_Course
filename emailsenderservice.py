class EmailSenderService():
    
    def __init__(self):
        self.emails = {}
        pass
    
    def send_mail(_user):
        from user import User
        mail = {
                "destinataire" : _user,
                "content" : "Attention, votre todo list est presque remplie !"
        }
        if(_user.is_valid()):
            _user.mails.append(mail)