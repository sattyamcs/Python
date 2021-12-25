# Wite a program to accept marks of 6 students and display them in a sorted manner?

m1 = int(input("marks of student number 1.  "))
m2 = int(input("marks of student number 2.  "))
m3 = int(input("marks of student number 3.  "))
m4 = int(input("marks of student number 4.  "))
m5 = int(input("marks of student number 5.  "))
m6 = int(input("marks of student number 6.  "))

marks = [m1,m2,m3,m4,m5,m6]
marks.sort()
print(marks)