# lib/helpers.py

from models.department import Department
from models.employee import Employee
import sys

# Helper functions for the CLI

def exit_program():
    """Exits the program."""
    print("Goodbye!")
    # Use sys.exit() to properly exit the program
    sys.exit()

# === DEPARTMENT HELPER FUNCTIONS (Code-Along) ===

def list_departments():
    """Gets all departments and prints them."""
    departments = Department.get_all()
    if departments:
        for department in departments:
            print(department)
    else:
        print("No departments found.")

def find_department_by_name():
    """Prompts for a name and finds and prints the matching department."""
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')

def find_department_by_id():
    """Prompts for an ID and finds and prints the matching department."""
    # use a trailing underscore not to override the built-in id function
    id_input = input("Enter the department's id: ")
    try:
        id_ = int(id_input)
    except ValueError:
        print("Invalid input. ID must be an integer.")
        return

    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')

def create_department():
    """Prompts for details, creates, and persists a new department."""
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)

def update_department():
    """Prompts for ID, new details, and updates the department."""
    id_input = input("Enter the department's id: ")
    try:
        id_ = int(id_input)
    except ValueError:
        print("Invalid input. ID must be an integer.")
        return

    department = Department.find_by_id(id_)
    if department:
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')

def delete_department():
    """Prompts for ID and deletes the matching department."""
    id_input = input("Enter the department's id: ")
    try:
        id_ = int(id_input)
    except ValueError:
        print("Invalid input. ID must be an integer.")
        return
        
    department = Department.find_by_id(id_)
    if department:
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')

# === EMPLOYEE HELPER FUNCTIONS (Lab Implementation) ===

# 7. List all employees
def list_employees():
    """Gets all employees stored in the database and prints each one."""
    employees = Employee.get_all()
    if employees:
        for employee in employees:
            print(employee)
    else:
        print("No employees found.")

# 8. Find employee by name
def find_employee_by_name():
    """Prompts for a name and finds and prints the matching employee."""
    name = input("Enter the employee's name: ")
    employee = Employee.find_by_name(name)
    
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")

# 9. Find employee by id
def find_employee_by_id():
    """Prompts for an id and finds and prints the matching employee."""
    id_input = input("Enter the employee's id: ")
    try:
        id_ = int(id_input)
    except ValueError:
        print("Invalid input. ID must be an integer.")
        return

    employee = Employee.find_by_id(id_)
    
    if employee:
        print(employee)
    else:
        print(f"Employee {id_} not found")

# 10. Create employee
def create_employee():
    """Prompts for details, creates, and persists a new Employee instance."""
    name = input("Enter the employee's name: ")
    job_title = input("Enter the employee's job title: ")
    
    try:
        department_id = int(input("Enter the employee's department id: "))
    except ValueError:
        print("Error creating employee: Department ID must be an integer.")
        return

    try:
        # Calls the Employee.create ORM method
        new_employee = Employee.create(name, job_title, department_id)
        print(f"Success: {new_employee}")
    except Exception as e:
        # Catches exceptions thrown by the property setters
        print(f"Error creating employee: {e}")

# 11. Update employee
def update_employee():
    """Prompts for ID, new details, and updates the employee."""
    id_input = input("Enter the employee's id: ")
    try:
        id_ = int(id_input)
    except ValueError:
        print("Invalid input. ID must be an integer.")
        return

    employee = Employee.find_by_id(id_)
    
    if not employee:
        print(f"Employee {id_} not found")
        return

    # If employee is found, prompt for new details and attempt update
    try:
        new_name = input("Enter the employee's new name: ")
        new_job_title = input("Enter the employee's new job title: ")
        
        # Read department ID and handle potential ValueError before setting property
        new_department_id_input = input("Enter the employee's new department id: ")
        new_department_id = int(new_department_id_input)

        # Use the property setters to validate and update the attributes
        employee.name = new_name
        employee.job_title = new_job_title
        employee.department_id = new_department_id

        # Persist changes to the database
        employee.update()
        print(f"Success: {employee}")

    except ValueError:
        # Handles case where department ID input is not a valid integer
        print("Error updating employee: Department ID must be an integer.")
    except Exception as e:
        # Catches exceptions thrown by property setters (validation errors)
        print(f"Error updating employee: {e}")


# 12. Delete employee
def delete_employee():
    """Prompts for ID and deletes the matching employee."""
    id_input = input("Enter the employee's id: ")
    try:
        id_ = int(id_input)
    except ValueError:
        print("Invalid input. ID must be an integer.")
        return

    employee = Employee.find_by_id(id_)
    
    if employee:
        employee.delete()
        print(f"Employee {id_} deleted")
    else:
        print(f"Employee {id_} not found")

# 13. List all employees in a department
def list_department_employees():
    """Prompts for department ID and lists all employees in that department."""
    department_id_input = input("Enter the department's id: ")
    try:
        department_id = int(department_id_input)
    except ValueError:
        print("Invalid input. ID must be an integer.")
        return

    # Find the department instance
    department = Department.find_by_id(department_id)

    if department:
        # Get the department's employees using the relationship method
        employees = department.employees() 
        if employees:
            for employee in employees:
                print(employee)
        else:
            print(f"Department {department_id} has no employees.")
    else:
        print(f"Department {department_id} not found")
pass