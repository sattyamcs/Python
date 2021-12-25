while(True):
    print ("print q to quit")
    a = input("enter a number: ")
    if a == "q":
        break
    try:                                           #this is used to run program well if error occurs it puts you to the exception directly
        print("trying...")
        a = int(a)
        if a>6:
            print("you entered a number greater than 6")
    except Exception as e:                               #runs the code without code intrruptions while this handles the exception with printing this   
        print(f"your input resulted in a error {e}")        #this will prints your error.

print("Thanks for playing this game")