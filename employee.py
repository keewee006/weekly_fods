'''Employee class and write/read from CSV with exception handling'''
import csv

class Employee:
    def __init__(self, empid, name, address, contact, spouse, children, salary):
        self.empid = empid
        self.name = name
        self.address = address
        self.contact = contact
        self.spouse = spouse
        self.children = children
        self.salary = salary

    def to_list(self):
        return [self.empid, self.name, self.address, self.contact, self.spouse, self.children, self.salary]

def save_employee(emp_list, filename='employees.csv'):
    try:
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['EmpID', 'Name', 'Address', 'Contact', 'Spouse', 'Children', 'Salary'])
            for emp in emp_list:
                writer.writerow(emp.to_list())
        print("Employee data saved.")
    except Exception as e:
        print("Error:", e)

def read_employees(filename='employees.csv'):
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print('\t'.join(row))
    except FileNotFoundError:
        print("File not found.")

# Example
emp1 = Employee("001", "Ram", "Pokhara", "98000000", "Rita", 2, 50000)
emp2 = Employee("002", "sita", "Lalitpur", "98001111", "Ravi", 0, 45000)
save_employee([emp1, emp2])
read_employees()
