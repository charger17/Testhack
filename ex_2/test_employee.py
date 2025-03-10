import unittest
from employee import Employee, EmployeeManager

class TestEmployeeManager(unittest.TestCase):

    def setUp(self):
        # Set up an employee manager instance and some employee instances for testing
        self.manager = EmployeeManager()
        self.employee1 = Employee("001", "Alice", "Developer", 70000, "Engineering")
        self.employee2 = Employee("002", "Bob", "Designer", 65000, "Design")
        self.employee3 = Employee("003", "Charlie", "Manager", 80000, "Engineering")

    def test_add_employee(self):
        # Test adding a new employee
        self.assertTrue(self.manager.add_employee(self.employee1))
        self.assertFalse(self.manager.add_employee(self.employee1))  # Duplicate employee ID

    def test_remove_employee(self):
        # Test removing an employee
        self.manager.add_employee(self.employee1)
        self.assertTrue(self.manager.remove_employee("001"))
        self.assertFalse(self.manager.remove_employee("001"))  # Already removed

    def test_update_employee_position(self):
        # Test updating an employee's position
        self.manager.add_employee(self.employee1)
        self.assertTrue(self.manager.update_employee_position("001", "Senior Developer"))
        self.assertEqual(self.manager.get_employee("001").position, "Senior Developer")
        self.assertFalse(self.manager.update_employee_position("004", "Intern"))  # Non-existent employee

    def test_update_employee_salary(self):
        # Test updating an employee's salary
        self.manager.add_employee(self.employee1)
        self.assertTrue(self.manager.update_employee_salary("001", 75000))
        self.assertEqual(self.manager.get_employee("001").salary, 75000)
        self.assertFalse(self.manager.update_employee_salary("004", 50000))  # Non-existent employee

    def test_get_employee(self):
        # Test retrieving an employee by their ID
        self.manager.add_employee(self.employee1)
        self.assertEqual(self.manager.get_employee("001"), self.employee1)
        self.assertIsNone(self.manager.get_employee("004"))  # Non-existent employee

    def test_search_employees_by_name(self):
        # Test searching employees by name
        self.manager.add_employee(self.employee1)
        self.manager.add_employee(self.employee2)
        self.manager.add_employee(self.employee3)
        self.assertEqual(len(self.manager.search_employees_by_name("alice")), 1)
        self.assertEqual(len(self.manager.search_employees_by_name("bob")), 1)
        self.assertEqual(len(self.manager.search_employees_by_name("charlie")), 1)
        self.assertEqual(len(self.manager.search_employees_by_name("john")), 0)

    def test_get_employees_by_department(self):
        # Test retrieving employees by department
        self.manager.add_employee(self.employee1)
        self.manager.add_employee(self.employee2)
        self.manager.add_employee(self.employee3)
        engineering_employees = self.manager.get_employees_by_department("Engineering")
        design_employees = self.manager.get_employees_by_department("Design")
        self.assertEqual(len(engineering_employees), 2)
        self.assertEqual(len(design_employees), 1)
        self.assertIn(self.employee1, engineering_employees)
        self.assertIn(self.employee3, engineering_employees)
        self.assertIn(self.employee2, design_employees)

    def test_add_multiple_employees(self):
        # Test adding multiple employees and checking their existence
        self.manager.add_employee(self.employee1)
        self.manager.add_employee(self.employee2)
        self.manager.add_employee(self.employee3)
        self.assertEqual(len(self.manager.employees), 3)
        self.assertIn("001", self.manager.employees)
        self.assertIn("002", self.manager.employees)
        self.assertIn("003", self.manager.employees)

    def test_remove_multiple_employees(self):
        # Test removing multiple employees and checking their existence
        self.manager.add_employee(self.employee1)
        self.manager.add_employee(self.employee2)
        self.manager.add_employee(self.employee3)
        self.manager.remove_employee("001")
        self.manager.remove_employee("002")
        self.assertEqual(len(self.manager.employees), 1)
        self.assertNotIn("001", self.manager.employees)
        self.assertNotIn("002", self.manager.employees)
        self.assertIn("003", self.manager.employees)

    def test_update_nonexistent_employee(self):
        # Test updating a non-existent employee
        self.assertFalse(self.manager.update_employee_position("004", "Intern"))
        self.assertFalse(self.manager.update_employee_salary("004", 50000))

    def test_get_all_employees(self):
        # Test retrieving all employees
        self.manager.add_employee(self.employee1)
        self.manager.add_employee(self.employee2)
        self.manager.add_employee(self.employee3)
        all_employees = self.manager.employees.values()
        self.assertIn(self.employee1, all_employees)
        self.assertIn(self.employee2, all_employees)
        self.assertIn(self.employee3, all_employees)

if __name__ == '__main__':
    unittest.main()