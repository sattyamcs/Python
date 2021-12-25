try:
    i = int(input("enter a number :"))
    c = 1/i
    print(c)
except Exception as e: 
    print(e)
    exit()
finally:                 
    print("we are done")       #this will run whatever happens to the program even with exceptions

print("The programme is done") #this runs when the code executed without error


