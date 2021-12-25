class Person:                        #class1 parent class
    country = "INDIA"
    def __init__(self):
        print("i am a person living in india\n")

    def takeBreathe(self):
        print("i am breathing")

class Employee:                      #class2 parent class
    company = "Honda"

    def __init__(self):
        super().__init__()           #this calls the constructor (__init__) of its parent class first then it prints itself
        print("i am a person living in india\n")

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreathe(self):
        print("i am luckly breathing")

class Programmer(Employee):          #class3 child class
    company = "fiber"

    def takeBreathe(self):
        super().takeBreathe()        #class2 is super class so it runs before itself
        print(f"i am breathing minorly, i cannt survive anymore")

p = Person()
p.takeBreathe()

e = Employee()
e.takeBreathe()

pr = Programmer()
pr.takeBreathe()     