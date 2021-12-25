class employee:
    company= "google"# attribute of class = class attributes
    salary = 100     # class attribute, that you defined here
 #  that is directly linked to the class

sattyam = employee()
hardy = employee()
sattyam.salary = 400              #object attribute that is made again.
hardy.salary = 300
print(sattyam.company)
print(hardy.company)               #here it prints google
print(sattyam.salary)              
print(hardy.salary)

# employee.company = "youtube"
# print(sattyam.company)
# print(hardy.company)               #here it prints youtube