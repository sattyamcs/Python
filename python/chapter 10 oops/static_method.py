class Employee:
    company = "facebook"
    def getsalary(self,signature): #we can pass m ore then self argument
         print(f"salary for the employee working in {self.company} is {self.salary}\n {signature}")

    @staticmethod    #this method is used as a decorater
    def greet():
        print("good morning sir")

    @staticmethod
    def time():
        print("the time is 9am in the morning")

sattyam = Employee()

sattyam.salary = 100000
sattyam.getsalary("thanks!") #here we passed signature argument. 
sattyam.greet()
sattyam.time()
# Employee.getsalary(sattyam) = sattyam.getsalary()
