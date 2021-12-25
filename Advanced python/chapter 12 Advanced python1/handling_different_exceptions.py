try:
    a = int(input("enter a number :"))
    c = 1/a
    print(c)

except ValueError as e:                 #this occurs when an unexceptional value is entered
    print("Please enter a valid value")

except ZeroDivisionError as e:          #this occurs with the value  dividing by 0
    print ("please sure you are dividing by 0")

print("Thanks for using this code!")
