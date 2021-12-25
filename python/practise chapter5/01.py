# ques. write a program to create a dictionary of hindi words with value as their english translation. provide user with an option to look it up?

myDict = { 
    "pankha" : "fan",
    "dabba" : "box",
    "vastu" : "item"

}
print("options are", myDict.keys())
a = input("enter the hindi words\n")
# print("the meaning of your word is:",myDict[a])

#below line will not through an error if the key is not present in dictionary
print("the meaning of your word is:",myDict.get(a))    
