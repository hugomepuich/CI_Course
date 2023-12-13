import unittest

class BehaviourTest(unittest.TestCase):
    
    # Tests the whole process
    def test_behaviour(self):
        
        # Creating valid user
        import user
        
        usr = user.User("Hugo", "Dautremepuich", "abcdEFGH1234", "hugo@hugo.fr", "04-08-1998")
        
        #it_bkp = None # will recieve an item that is supposed to fail bc same date
        
        # Will create an item each days for 7 days
        import item, todolist
        for i in range(7):
            it = item.Item("item_"+str(i), "content")
            it.alter_time(1 + i)
            self.assertTrue(todolist.ToDoList.add_item(usr, it))
            
            if(i == 6):
                it_bkp = item.Item("item_piege", "content")
                it_bkp.alter_time(1 + i)
        
        # This should not work
        # we are trying to add an item with the same date as the last one 
        self.assertFalse(todolist.ToDoList.add_item(usr, usr.to_do_list._list[-1]))
        
        # This should not work either
        
        it_same_name = item.Item("item_0", "content")
        it_same_name.alter_time(10) # 10 days after the first item so we are sure it's the name that fails
        
        self.assertFalse(todolist.ToDoList.add_item(usr, it_same_name))
        
        # This should work
        last_item = item.Item("item_7", "content")
        last_item.alter_time(10)
        
        # Adding 8th item
        self.assertTrue(todolist.ToDoList.add_item(usr, last_item))
        
        # Checking if we got a mail
        self.assertTrue(len(usr.mails) > 0)
        
        import savesystem
        sys = savesystem.SaveSystem()
        
        # Checking the save system (should raise exeptions every time)
        for i in range(len(usr.to_do_list._list)):
            self.assertRaises(savesystem.SaveException, sys.save, usr, usr.to_do_list._list[i])