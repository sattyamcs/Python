# create a class with a class attribute a, create an object from it and set a directly using object  a=0
# doesthis changes the class attribute?

class Sample:
    a = "sattyam"

obj = Sample()
obj.a = "vicky"        # this sets a new instance attribute
# Sample.a = "vicky"    this will change the class attribute

print(Sample.a)
print(obj.a)

# no,it does not changed . it created a instance attribute, it does not change the class attribute