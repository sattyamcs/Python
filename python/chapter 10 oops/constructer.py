class Employee:
    company = "facebook"

    def __init__(self,name,salary,subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("employee is created")

    def getDetails(self):
        print(f"the name of the employee is {self.name}")
        print(f"the salary of the employee is {self.salary}")
        print(f"the subunit of the employee is {self.subunit}")

    def getsalary(self,signature): #we can pass more then self argument
         print(f"salary for the employee working in {self.company} is {self.salary} \n {signature}")

    @staticmethod    #this method is used as a decorater
    def greet():
        print("good morning sir")

    @staticmethod
    def time():
        print("the time is 9am in the morning")

sattyam = Employee("harry",10000,"youtube")
# sattyam.getDetails()
sattyam.getsalary("sattyam")

