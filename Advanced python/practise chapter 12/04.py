# write a program to display a/b where A and b are integers . if b=0 display infinite by handling the zerodivision error?
a = int(input("Enter number a : "))
b = int(input("Enter number b : "))

try:
    print(a/b)

except:
    print("infinite")