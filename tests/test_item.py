import unittest
import item

i_valid = item.Item("item1", "content")
i_invalid_name = item.Item("", "content")
i_invalid_content = item.Item("item2", "")

class Test_Item(unittest.TestCase):
    
    def test_valid_name(self):
        self.assertTrue(i_valid.is_valid_name(i_valid.name, []))
        
    def test_valid_content(self):
        self.assertTrue(i_valid.is_valid_content(i_valid.content))
        
    def test_no_name(self):
        self.assertFalse(i_invalid_name.is_valid_name(i_invalid_name.name, []))
        
    def test_no_content(self):
        self.assertFalse(i_invalid_content.is_valid_content(i_invalid_content.content))