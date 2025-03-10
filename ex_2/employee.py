class Employee:
    def __init__(self, employee_id, name, position, salary, department):
        # Constructor to initialize an employee with ID, name, position, salary, and department
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary
        self.department = department

class EmployeeManager:
    def __init__(self):
        # Constructor to initialize the employee manager with an empty dictionary of employees
        self.employees = {}

    def add_employee(self, employee):
        # Adds an employee to the manager if the employee ID is not already present
        if employee.employee_id in self.employees:
            return False
        self.employees[employee.employee_id] = employee
        return True

    def remove_employee(self, employee_id):
        # Removes an employee from the manager by their ID
        if employee_id in self.employees:
            del self.employees[employee_id]
            return True
        return False

    def update_employee_position(self, employee_id, new_position):
        # Updates the position of an employee
        if employee_id in self.employees:
            self.employees[employee_id].position = new_position
            return True
        return False

    def update_employee_salary(self, employee_id, new_salary):
        # Updates the salary of an employee
        if employee_id in self.employees:
            self.employees[employee_id].salary = new_salary
            return True
        return False

    def get_employee(self, employee_id):
        # Retrieves an employee by their ID
        return self.employees.get(employee_id, None)

    def search_employees_by_name(self, name):
        # Searches for employees by name (case-insensitive)
        return [employee for employee in self.employees.values() if name.lower() in employee.name.lower()]

    def get_employees_by_department(self, department):
        # Retrieves all employees in a specific department
        return [employee for employee in self.employees.values() if employee.department == department]