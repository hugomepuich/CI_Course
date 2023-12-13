class Item:
    
    def __init__(self, name, content):
        import datetime
        self.name = name
        self.content = content
        self.creation_date = datetime.datetime.now()
        
    
    def is_valid_name(self, name, _list):
        unique = True
        for i in _list:
            if i.name == name:
                unique = False
                break
        return unique and len(name) > 0
    
    def is_valid_content(self, content):
        return len(content) > 0 and len(content) <= 1000
        
    def alter_time(self, days):
        import datetime
        self.creation_date = self.creation_date + datetime.timedelta(days)