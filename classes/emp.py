class Employee:

    num_of_emps = 0
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self. pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullName(self): # functions to print full name
        return '{} {}'.format(self.first, self.last)

# Developer class, inherits first, last, pay
class developer(Employee):
    # changes pay raise
    raise_amt = 1.15

    # and initials its own variable 'prog_lang' with super()
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay) 
        self.prog_lang = prog_lang

class manager(Employee):
    # same, but now create an employee list
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    # adds employee to list
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    # removes
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    # prints
    def print_emps(self):
        for emp in self.employees:
            print('--->', emp.fullName())


# creates employees
emp_1 = Employee('emp1','Test', 9000)
emp_2 = Employee('emp2','Test', 2200)

# creates developers
dev_1 = developer('dev1','Testa', 6000, 'Java')
dev_2 = developer('dev1','Test', 6000, 'Python')

# creates manager and adds developers to its list
mgr_1 = manager('Manager1', 'test', 90111, [dev_1])


print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

#print(emp_1)



#print('{} {}'.format(emp_1.first, emp_1.last))
#print('{} {}'.format(emp_2.first, emp_2.last))

## same thing 
#print(emp_1.fullName())
#print(emp_2.fullName())




