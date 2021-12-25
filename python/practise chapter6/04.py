# ques. write a program to find whether a given username contains 10 characters or not

username = input("enter your username\n")

if(len(username)<=10):
    print("contain less than 10char")              #using len function, len(username)
elif(len(username)>=10):
    print("contain more than 10character")
else:
    print("contain 10 character")
print("Thanqu for doing this!")