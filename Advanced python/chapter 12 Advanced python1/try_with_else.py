try:
    i = int(input("enter a number :"))
    c = 1/i
    print(c)
except Exception as e: #this will run when try not runs
    print(e)
else:                #this will excecute only when the try runs successfully. 
    print("the code is successfully run")