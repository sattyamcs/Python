class Employee:
    company = "bharat gas"
    salary = 5600
    salarybonus =500
    # totalSalary = 6100

    @property                                      #here we use property decorater also called getter method
    def totalSalary(self):
        return self.salary + self.salarybonus

    @totalSalary.setter                             #setter is used after name that is given
    def totalSalary(self,val):
        self.salarybonus = val - self.salary

e = Employee()
print(e.totalSalary)
e.totalSalary = 5800         # setter will change the total salary to salary and bonus
print(e.salary)
print(e.salarybonus)
