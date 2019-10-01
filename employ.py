import datetime

class employee:
    def __init__(self,birthDate,accountNum,monthSalary):
        self._birthDate = birthDate
        self._accountNum = accountNum
        self._monthSalary = monthSalary = 0
        self._hourWorked = 0
        self._hourlySalary = 0

    def SetMonthSalary(self, salary):
        self._monthSalary = salary

    def setHourlySalary():
        self._hourWorked = hoursWorked
        self._hourlySalary = hourSalary

    def createSalaryTrans():
        salary = 0
        if self._hoursWorked == 0:
            salary = self._hourlyWorked * self._hourlySalary
        elif soldFor > 0:
            salary = self._monthSalary + self_soldFor * 0.02
        else:
            salary = self._monthSalary

        return f"{self._accountNum} {Self._monthSalary}"



lista = []

lista.append(employee(datetime.date(1972,8,3),"12345",12000))
lista.append(employee(datetime.date(1972,8,3),"123322345",11000))
lista.append(employee(datetime.date(1972,8,3),"123432325",500))

for employee in lista:
    print(employee.createSalaryTrans())
