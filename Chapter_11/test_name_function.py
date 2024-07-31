import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    '''Tests for the name_function.py'''

    def test_first_last_name(self):
        formatted_name = get_formatted_name('christopher' , 'holcombe')
        self.assertEqual(formatted_name, 'Christopher Holcombe')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('christopher', 'james', 'holcombe')
        self.assertEqual(formatted_name, 'Christopher Holcombe James')

unittest.main()