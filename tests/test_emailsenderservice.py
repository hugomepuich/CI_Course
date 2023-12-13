import unittest, emailsenderservice

class EmailSenderService_Test(unittest.TestCase):
    
    def test_send_mail(self):
        import user
        
        # valid user
        u = user.User("Hugo", "Dautremepuich", "abcdEFGH1234", "hugo@hugo.fr", "04-08-1998")
        emailsenderservice.EmailSenderService.send_mail(u)
        self.assertGreater(len(u.mails), 0)