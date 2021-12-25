# ques. write a program to calculate the factorial of a given number using for Loop?

# factorials are #n! = 1 x 2 x 3 x 4 x 5 x ....
# #   5! = 1 x 2 x 3 x 4 x 5 

num = int(input("enter your number: "))
factorial = 1
for i in range (1, num+1):
    factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")
    