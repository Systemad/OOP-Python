class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self. pay = pay
        self.email = first + '.' + last + '@gmail.com'

    def fullName(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Dan','Test', 9000)
emp_2 = Employee('Hej','Test', 2200)

#print(emp_1)



#print('{} {}'.format(emp_1.first, emp_1.last))
#print('{} {}'.format(emp_2.first, emp_2.last))

## same thing 
print(emp_1.fullName())
print(emp_2.fullName())

