class Employee:
    company = "facebook"
    def getsalary(self): #self is a parameter that passed automatically
         print(f"salary for the employee working in {self.company} is {self.salary}")

sattyam = Employee()
sattyam.salary = 100000
sattyam.getsalary()
# Employee.getsalary(sattyam) = sattyam.getsalary()
