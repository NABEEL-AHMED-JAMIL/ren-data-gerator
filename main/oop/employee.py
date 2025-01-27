class Employee:

    company_name = "Tech Corp" # Class variable

    def __init__(self, name):
        self.name = name # Instance variable

# Employ detail
if __name__ == '__main__':
    emp = Employee("alice")
    print(emp.name)
    print(emp.company_name)
    print(Employee.company_name)