'''Student class with attributes and display method'''
class Student:
    def __init__(self, id, name, address, year, level, section):
        self.id = id
        self.name = name
        self.address = address
        self.year = year
        self.level = level
        self.section = section

    def display(self):
        print(f"ID: {self.id}, Name: {self.name}, Address: {self.address}")
        print(f"Admission Year: {self.year}, Level: {self.level}, Section: {self.section}")

# Example
s = Student("001", "ram", "Kathmandu", 2023, "Bachelor", "A")
s.display()
