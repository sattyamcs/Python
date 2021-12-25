'''write a program to input names, marks and phone number of a student and format it using the format function like below
 The name of the student is sattyam , his marks are 72 and phone number is 945562123'''

name = input("Enter your name :")
marks = int(input("enter your marks :"))
phone = int(input(" Enter your mobile number :"))

a="The name of the student is {}. Marks he got is {}. His mobile number is {}".format(name,marks,phone)
print(a)