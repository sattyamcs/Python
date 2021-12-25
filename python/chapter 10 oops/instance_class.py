class employee:
    company= "google"
    salary = 100     

sattyam = employee()       #object intantiation
hardy = employee()


#creating instance attribute salary for both object. program always prints instance attribues if not available then it goes to class attributes

sattyam.salary = 400              
hardy.salary = 300
print(sattyam.salary)              
print(hardy.salary)

# if instance attribute is not found then it shows only the class attributes. it wil show 100

sattyam.address()
# throws an error because no instance attribute or class attribute is found.