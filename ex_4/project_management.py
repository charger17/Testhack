class Task:
    def __init__(self, task_id, name, description, status="Pending"):
        # Constructor to initialize a task with ID, name, description, and status
        self.task_id = task_id
        self.name = name
        self.description = description
        self.status = status
        self.assigned_to = None

class Employee:
    def __init__(self, employee_id, name, position):
        # Constructor to initialize an employee with ID, name, and position
        self.employee_id = employee_id
        self.name = name
        self.position = position

class Project:
    def __init__(self, project_id, name, description):
        # Constructor to initialize a project with ID, name, and description
        self.project_id = project_id
        self.name = name
        self.description = description
        self.tasks = []

    def add_task(self, task):
        # Adds a task to the project
        self.tasks.append(task)

    def remove_task(self, task_id):
        # Removes a task from the project by its ID
        self.tasks = [task for task in self.tasks if task.task_id != task_id]

    def get_task(self, task_id):
        # Retrieves a task from the project by its ID
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

class ProjectManager:
    def __init__(self):
        # Constructor to initialize the project manager with empty dictionaries for projects and employees
        self.projects = {}
        self.employees = {}

    def add_project(self, project):
        # Adds a project to the manager if the project ID is not already present
        if project.project_id in self.projects:
            return False
        self.projects[project.project_id] = project
        return True

    def remove_project(self, project_id):
        # Removes a project from the manager by its ID
        if project_id in self.projects:
            del self.projects[project_id]
            return True
        return False

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

    def assign_task_to_employee(self, project_id, task_id, employee_id):
        # Assigns a task to an employee
        project = self.projects.get(project_id)
        employee = self.employees.get(employee_id)
        if project and employee:
            task = project.get_task(task_id)
            if task:
                task.assigned_to = employee
                return True
        return False

    def update_task_status(self, project_id, task_id, status):
        # Updates the status of a task
        project = self.projects.get(project_id)
        if project:
            task = project.get_task(task_id)
            if task:
                task.status = status
                return True
        return False

    def generate_project_report(self, project_id):
        # Generates a report for a project with task details and their statuses
        project = self.projects.get(project_id)
        if project:
            report = {
                "project_id": project.project_id,
                "project_name": project.name,
                "tasks": []
            }
            for task in project.tasks:
                report["tasks"].append({
                    "task_id": task.task_id,
                    "task_name": task.name,
                    "status": task.status,
                    "assigned_to": task.assigned_to.name if task.assigned_to else None
                })
            return report
        return None