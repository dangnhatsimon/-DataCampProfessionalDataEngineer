class Employee:
    def __init__(self, name, salary=0):
        self.name = name
    # Check if salary is positive
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")

    def set_name(self, new_name):
        self.name = new_name

    def set_salary(self, new_salary):
        self.salary = new_salary 

    # Add a give_raise() method with amount as an argument
    def give_raise(self, amount):
        self.salary = self.salary + amount

    def monthly_salary(self):
        return self.salary / 12

# Create the emp object
emp = Employee()
emp.set_name('Korel Rossi')
emp.set_salary(50000)

# Print the salary
print(emp.salary)

# Give emp a raise of 1500
emp.give_raise(1500)
print(emp.salary)


class Employee:
    MIN_SALARY = 30000    

    def __init__(self, name, salary=MIN_SALARY):
        self.name = name
        if salary >= Employee.MIN_SALARY:
            self.salary = salary
        else:
            self.salary = Employee.MIN_SALARY

    def give_raise(self, amount):
        self.salary += amount      


# Define a new class Manager inheriting from Employee
class Manager(Employee):
    def display(self):
        print("Manager ", self.name)

    def __init__(self, name, salary=50000, project=None):
        Employee.__init__(self, name, salary)
        self.project = project

    # Add a give_raise method
    def give_raise(self, amount, bonus=1.05):
        new_amount = amount * bonus
        Employee.give_raise(self, new_amount)


# Define a Manager object
mng = Manager("Debbie Lashko", 86500)

# Print mng's name
print(mng.name)


class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    # Add the __repr__() method  
    def __repr__(self):
        return f"Employee('{self.name}', {self.salary})" 


emp1 = Employee("Amar Howard", 30000)
print(repr(emp1))
emp2 = Employee("Carolyn Ramirez", 35000)
print(repr(emp2))


class Employee:
    def __init__(self, name, salary=30000):
        self.name, self.salary = name, salary

    # Add the __str__() method
    def __str__(self):
        emp_str = f"""Employee name: {self.name}
Employee salary: {self.salary}"""
        return emp_str


emp1 = Employee("Amar Howard", 30000)
print(emp1)
emp2 = Employee("Carolyn Ramirez", 35000)
print(emp2)