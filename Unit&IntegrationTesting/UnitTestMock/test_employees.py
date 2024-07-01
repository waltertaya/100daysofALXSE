import unittest
from unittest.mock import Mock, patch

from employees import EmployeeAPI

class TestEmployees(unittest.TestCase):

    @patch("requests.get")
    def test_get_employee_details(self, mock_get):
        mock_response = Mock()
        response_dict = {
            'employee_id': 891,
            'fullname': 'Brett Cooper',
            'salary_per_month': 123000,
            'department': 'IT',
            'level': 'Senior Developer',
            'Date_hired': '22nd May 2012'
        }

        mock_response.json.return_value = response_dict
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        employee = EmployeeAPI()
        result = employee.get_employee_details(891)

        mock_get.assert_called_with('https://api.example.com/employees/891')
        self.assertEqual(result, response_dict)
        print(f'Mock Response: {mock_response}   Mock Get: {mock_get}')

if __name__ == '__main__':
    unittest.main()
