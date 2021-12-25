# create a class employee and add salary and increment properties to it . write a method of salary increment 
# with @property decorater with a setter which changes the value of increment based on the slary?

class Employee:
    salary = 1000
    increment = 1.5
    @property
    def salaryAfterincrement(self):
        return self.salary*self.increment

    @salaryAfterincrement.setter
    def salaryAfterincrement(self,sai):
        self.increment = sai/self.salary

e = Employee()
print(e.salaryAfterincrement)
e.salaryAfterincrement = 2000
print(e.increment)