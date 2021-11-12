from employee import Employee
import unittest
from unittest.mock import patch


class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.test_data = Employee('Jane', 'Smith', 1109)

    def test_email(self):
        self.assertEqual(self.test_data.email, 'Jane.Smith@email.com')

    def test_fullname(self):
        self.assertEqual(self.test_data.fullname, 'Jane Smith')

    def test_apply_raise(self):
        self.test_data.apply_raise()
        self.assertEqual(self.test_data.pay, 1164)

    @patch('employee.requests.get')
    def test_monthly_schedule(self, mock_get):
        mock_get.return_value.ok = True
        mock_get.return_value.text = 'ok = true'
        response = self.test_data.monthly_schedule('May')
        print(response)
        self.assertEqual(response, 'ok = true')
        mock_get.return_value.ok = False
        response = self.test_data.monthly_schedule('May')
        print(response)
        self.assertEqual(response, 'Bad Response!')
        
        
if __name__ == '__main__':
    unittest.main()
