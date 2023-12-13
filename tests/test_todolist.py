import unittest, user, todolist, item

valid_user = user.User("Hugo", "Dautremepuich", "abcdEFGH1234", "hugo@hugo.fr", "04-08-1998")
invalid_user = user.User("Hugo", "Dautremepuich", "ABCDEFGHIJ", "hugo@hugo.fr", "04-08-1998")

class ToDoList_test(unittest.TestCase):
    
    # Testing good item with good user with empty list
    def test_add_item(self):
        i = item.Item("item1", "content")
        self.assertTrue(todolist.ToDoList.add_item(valid_user, i))
        self.assertTrue(len(valid_user.to_do_list._list) > 0)
    
    # Testing good item with bad user
    def test_add_item_invalid_user(self):
        i = item.Item("item1", "content")
        
        #invalid user
        u = user.User("Hugo", "Dautremepuich", "ABCDEFGHIJ", "hugo@hugo.fr", "04-08-1998")
        self.assertFalse(todolist.ToDoList.add_item(u, i))
        
    # Testing good user with bad item (name)
    def test_add_item_invalid_name(self):
        i = item.Item("", "content")
        
        # valid user
        u = user.User("Hugo", "Dautremepuich", "abcdEFGH1234", "hugo@hugo.fr", "04-08-1998")
        self.assertFalse(todolist.ToDoList.add_item(u, i))
        
    # Testing good user with bad item (content)
    def test_add_item_invalid_content(self):
        i = item.Item("item1", "")
        
        # valid user
        u = user.User("Hugo", "Dautremepuich", "abcdEFGH1234", "hugo@hugo.fr", "04-08-1998")
        self.assertFalse(todolist.ToDoList.add_item(u, i))
        
    # Testing good item with good user with full list
    def test_add_item_full_list(self):
        i = item.Item("item1", "content")
        
        # Creating full list
        _list = todolist.ToDoList()
        for j in range(10):
            _list._list.append(item.Item("item"+str(j), "content"))
            
        # valid user
        u = user.User("Hugo", "Dautremepuich", "abcdEFGH1234", "hugo@hugo.fr", "04-08-1998")
        u.to_do_list = _list
        self.assertFalse(todolist.ToDoList.add_item(u, i))
    
    # Test mail got received
    def test_sends_mail_at_eight(self):
        i = item.Item("aaa", "content")
        
        _list = todolist.ToDoList()
        for j in range(7):
            _list._list.append(item.Item("item"+str(j), "content"))
        
        u = user.User("Hugo", "Dautremepuich", "abcdEFGH1234", "hugo@hugo.fr", "04-08-1998")
        u.to_do_list = _list
        i.alter_time(1) # it will not work if we do it right away
        
        todolist.ToDoList.add_item(u, i)
        self.assertTrue(len(u.mails))
        
    # Test can't if two same name
    def test_add_twice_same_name(self):
        u = user.User("Hugo", "Dautremepuich", "abcdEFGH1234", "hugo@hugo.fr", "04-08-1998")
        i = item.Item("superitem", "content")
        self.assertTrue(todolist.ToDoList.add_item(u, i))
        i2 = item.Item("superitem", "content")
        i2.alter_time(1) # it will not work anyway if we do it right away
        self.assertFalse(todolist.ToDoList.add_item(u, i2))