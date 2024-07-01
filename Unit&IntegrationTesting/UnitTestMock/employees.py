import requests

class EmployeeAPI:

    def get_employee_details(self, employee_id):
        response = requests.get(f"https://api.example.com/employees/{employee_id}")
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
