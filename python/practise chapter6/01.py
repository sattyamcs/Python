# ques1. write a programme to find greatest of four numbers entered by the user


num1 = int(input("enter number 1 \n"))
num2 = int(input("enter number 2 \n"))
num3 = int(input("enter number 3 \n"))
num4 = int(input("enter number 4 \n"))

if(num1>num4):
    f1=num1
else:
    f1=num4

if(num2>num3):
    f2=num2
else:
    f2=num4

if(f1>f2):
    print(str(f1)+"is the greatest")
else:
    print( str(f2)+"is larget")

