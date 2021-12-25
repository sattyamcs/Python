# this mainly occurs when the child class is inherited from more then one parent class

class Employee:                            #class1 , parent class
    company = "visa"
    ecode = 120
class Freelancer:                          # class2 , parent class
    company = "fiber"
    level = 0
    def upgradeLevel(self):
        self.level = self.level+1


class Programmer(Employee,Freelancer):      #class3, childclass . here we can carry all the methods and properties of class1 and class2
    name = "rohit"

p = Programmer()                            
p.upgradeLevel()                             
print(p.level)
print(p.company)          #here the priorities are given to the class that first written in class programmer