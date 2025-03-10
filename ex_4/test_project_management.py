import unittest
from project_management import Task, Employee, Project, ProjectManager

class TestProjectManager(unittest.TestCase):

    def setUp(self):
        # Set up a project manager instance and some project, task, and employee instances for testing
        self.manager = ProjectManager()
        self.project1 = Project("P001", "Project One", "Description of Project One")
        self.project2 = Project("P002", "Project Two", "Description of Project Two")
        self.task1 = Task("T001", "Task One", "Description of Task One")
        self.task2 = Task("T002", "Task Two", "Description of Task Two")
        self.employee1 = Employee("E001", "Alice", "Developer")
        self.employee2 = Employee("E002", "Bob", "Designer")

    def test_add_project(self):
        # Test adding a new project
        self.assertTrue(self.manager.add_project(self.project1))
        self.assertFalse(self.manager.add_project(self.project1))  # Duplicate project ID

    def test_remove_project(self):
        # Test removing a project
        self.manager.add_project(self.project1)
        self.assertTrue(self.manager.remove_project("P001"))
        self.assertFalse(self.manager.remove_project("P001"))  # Already removed

    def test_add_employee(self):
        # Test adding a new employee
        self.assertTrue(self.manager.add_employee(self.employee1))
        self.assertFalse(self.manager.add_employee(self.employee1))  # Duplicate employee ID

    def test_remove_employee(self):
        # Test removing an employee
        self.manager.add_employee(self.employee1)
        self.assertTrue(self.manager.remove_employee("E001"))
        self.assertFalse(self.manager.remove_employee("E001"))  # Already removed

    def test_assign_task_to_employee(self):
        # Test assigning a task to an employee
        self.manager.add_project(self.project1)
        self.manager.add_employee(self.employee1)
        self.project1.add_task(self.task1)
        self.assertTrue(self.manager.assign_task_to_employee("P001", "T001", "E001"))
        self.assertEqual(self.project1.get_task("T001").assigned_to, self.employee1)
        self.assertFalse(self.manager.assign_task_to_employee("P001", "T003", "E001"))  # Non-existent task
        self.assertFalse(self.manager.assign_task_to_employee("P001", "T001", "E003"))  # Non-existent employee

    def test_update_task_status(self):
        # Test updating the status of a task
        self.manager.add_project(self.project1)
        self.project1.add_task(self.task1)
        self.assertTrue(self.manager.update_task_status("P001", "T001", "Completed"))
        self.assertEqual(self.project1.get_task("T001").status, "Completed")
        self.assertFalse(self.manager.update_task_status("P001", "T003", "Completed"))  # Non-existent task

    def test_generate_project_report(self):
        # Test generating a project report
        self.manager.add_project(self.project1)
        self.manager.add_employee(self.employee1)
        self.project1.add_task(self.task1)
        self.manager.assign_task_to_employee("P001", "T001", "E001")
        report = self.manager.generate_project_report("P001")
        self.assertEqual(report["project_id"], "P001")
        self.assertEqual(report["project_name"], "Project One")
        self.assertEqual(len(report["tasks"]), 1)
        self.assertEqual(report["tasks"][0]["task_id"], "T001")
        self.assertEqual(report["tasks"][0]["task_name"], "Task One")
        self.assertEqual(report["tasks"][0]["status"], "Pending")
        self.assertEqual(report["tasks"][0]["assigned_to"], "Alice")

if __name__ == '__main__':
    unittest.main()