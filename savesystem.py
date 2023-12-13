class SaveException(Exception):
    def __init__(self, message):
        self.message = message

class SaveSystem():
    
    def __init__(self):
        self.storage = {}
    
    def save(self, _user, item):
        # elle doit simplement lever une exception
        e = SaveException("Save did fail")
        raise e