class Employee:
    company = "camel"
    salary = 100
    location ="delhi"

    # def changeSalary(self,sal):
    #     self__class__salary = sal

    @classmethod
    def changeSalary(cls,sal):      #class method , this will change the attribute of class
        cls.salary = sal



e = Employee()
print(e.salary)
e.changeSalary(200)
print(Employee.salary)
