# ques2. write a programe to find out whether a student is pass or fail, 
# if it requires total 40% and atleast 33% in each subject to pass . 
# assume 3 subjects and take marks as an input from the user

sub1 = int(input("enter first subject marks\n"))
sub2 = int(input("enter second subject marks\n"))
sub3 = int(input("enter third subject marks\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are failed due to less than 33% marks in one of the subject")

elif(sub1+sub2+sub3)/3 <40:
    print("you are failed due to total percentage is less than 40%")

else:
    print("congratulatons, you are passed!")
    