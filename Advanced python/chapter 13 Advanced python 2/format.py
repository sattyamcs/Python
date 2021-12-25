name = "sattyam"
channel = "python learner"
type = "coder"

print(f"my name is {name} and my channel is{channel}") #this is normal f string we used 
a ="my name is {} and my channel is{}".format(name,channel) #this is format method
a ="my name is {1} and my channel is{0} and i am a {2}".format(name,channel,type) #this will change the value with index number
print(a)