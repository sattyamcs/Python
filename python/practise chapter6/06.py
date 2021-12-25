# ques. write a program to calculate the grade of a student from his marks from the following scheme?

marks = int(input("enter your marks\n"))

if marks>=90:
    grade="A"
elif marks>=80:
    grade="B"
elif marks>=70:
    grade="c"
elif marks>=60:
    grade="D"
elif marks>=50:
    grade="E"
else:
    grade="failed"

print("You have got",grade)
