class ToDoList:
    
    def __init__(self, owner):
        self._list = []
        self.owner = owner
        
    def __init__(self):
        self._list = []
        self.owner = None
        
    def add_item(_user, item):
        if not item.is_valid_name(item.name, _user.to_do_list._list) or not item.is_valid_content(item.content):
            return False
        
        _list = _user.to_do_list
        
        if not _user.is_valid():
            return False
        
        if len(_list._list) < 10:
            import datetime
            now = datetime.datetime.now()
            
            if(len(_list._list) == 0):
                _list._list.append(item)
                return True
            delta = now - (_list._list[-1].creation_date)
            if (delta.days / 24 / 60 < 30):
                _list._list.append(item)
                if(len(_list._list) == 8):
                    import emailsenderservice
                    emailsenderservice.EmailSenderService.send_mail(_user)
                return True
            else:
                return False
        return False
    
    def save_item(_user, item):
        import savesystem
        savesystem.SaveSystem.save_item(_user, item)
    