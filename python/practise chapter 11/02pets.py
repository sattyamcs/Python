# create a class pet from a class animals and further create class dog from pets . add a method back to class dog?
# this is a kind of multilevel inheritance parent > child >child.

class Animals:
    animalsType = "mammals"

class Pet:
    colour ="white"

class Dog:
    @staticmethod         #This is not using self (class or instance attribute) thats y we use static method
    def bark():
        print("bow bow")    

d = Dog
d.bark()