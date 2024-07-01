# unittest.mock - mock object library

- Mock object are fake object that helps decide whether a test failed or passed by verifying whether an interaction with an object occurred.

- It allows you to replace parts of your system under test with mock objects and make assertions about how they have been used.

- `unittest.mock` provides a core `Mock` class removing the need to create a host of stubs throughout your test suite. After performing an action, you can make assertions about which methods / attributes were used and arguments they were called with. You can also specify return values and set needed attributes in the normal way.

Sure! Let's break down how mocking works in unit testing, specifically using the `unittest.mock` module in Python, and how it's applied in your test case.

### What is Mocking?

Mocking is a technique used in unit testing to replace real objects with simulated ones that mimic their behavior. This is useful when you want to isolate the code being tested and control the environment it runs in.

### Key Concepts

1. **Mock Object**: A mock object is a simulated object that mimics the behavior of real objects in controlled ways.
2. **Patching**: Patching is the process of replacing an object in your code with a mock object during a test.

### Code Breakdown

1. **Import Statements**

```python
import unittest
from unittest.mock import Mock, patch
from employees import EmployeeAPI
```
   - `unittest` is Python's built-in library for creating and running tests.
   - `Mock` and `patch` are from `unittest.mock`, used for creating mock objects and patching respectively.
   - `EmployeeAPI` is the class you're testing, presumably defined in `employees.py`.

2. **Test Class Definition**

```python
class TestEmployees(unittest.TestCase):
```
   - This defines a test class that inherits from `unittest.TestCase`.

3. **Patching the requests.get Method**

```python
@patch("requests.get")
def test_get_employee_details(self, mock_get):
```
   - The `@patch("requests.get")` decorator replaces the `requests.get` method with a mock object for the duration of the test method.
   - `mock_get` is the mock object that will replace `requests.get`.

4. **Creating a Mock Response**

```python
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
```
   - `mock_response = Mock()` creates a mock object to simulate the response object returned by `requests.get`.
   - `response_dict` is a dictionary that mimics the JSON response you expect from the API.
   - `mock_response.json.return_value = response_dict` sets the mock object's `json` method to return `response_dict`.
   - `mock_response.status_code = 200` sets the mock object's `status_code` attribute to 200, simulating a successful HTTP response.
   - `mock_get.return_value = mock_response` sets the return value of the patched `requests.get` method to be the `mock_response`.

5. **Calling the Method Under Test**

```python
    employee = EmployeeAPI()
    result = employee.get_employee_details(891)
```
   - An instance of `EmployeeAPI` is created.
   - `employee.get_employee_details(891)` is called. Since `requests.get` is patched, it returns `mock_response` instead of making an actual HTTP request.

6. **Assertions**

```python
    mock_get.assert_called_with('https://api.example.com/employees/891')
    self.assertEqual(result, response_dict)
```
   - `mock_get.assert_called_with('https://api.example.com/employees/891')` checks that `requests.get` was called with the correct URL.
   - `self.assertEqual(result, response_dict)` verifies that the method's return value matches the expected dictionary.

7. **Running the Test**

```python
if __name__ == '__main__':
    unittest.main()
```
   - This runs all the test cases defined in the file when the script is executed directly.

### Summary

- **Patching**: Temporarily replaces `requests.get` with a mock during the test.
- **Mock Object**: `mock_response` simulates the real HTTP response.
- **Assertions**: Verifies the behavior of `get_employee_details` and checks the interaction with the mocked `requests.get`.

Mocking allows you to control the environment in which your code runs, making it possible to test how your code handles different scenarios without relying on external services.


## Author

- **@waltertaya**
