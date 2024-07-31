import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Create an employee instance for use in the tests."""
        self.employee = Employee('John', 'Doe', 50000)

    def test_give_default_raise(self):
        """Test the default raise amount."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """Test a custom raise amount."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 60000)

if __name__ == '__main__':
    unittest.main()
