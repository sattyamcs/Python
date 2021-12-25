# write a class train that has methods to book tickets , get status (no. of seats) and get fare informations 
# of train running under indian railways?

class Train:
    def __init__(self,name,fare,seats):
        self.name = name 
        self.fare = fare 
        self.seats = seats 

    def getStatus(self):          
        print("*******")
        print(f"the name of the train is {self.name}")
        print(f"the fare of the train is RS {self.fare}")
        print(f"the seats available  in the train is {self.seats}")
        print("***********")

    def bookticket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! your seat number is {self.seats} and your fare for the ticket is {self.fare}")
            self.seats = self.seats - 1         #update the seat number
        else:
            print("seats are not avialable, please visit tatkal")
  
intercity = Train("intercity express : 14005",300,5)
intercity.getStatus()
intercity.bookticket()
intercity.getStatus()