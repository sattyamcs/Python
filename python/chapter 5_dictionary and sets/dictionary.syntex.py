myDict = {"fast": "a quick manner",               
"sattyam": "a coder",                               #key:sattyam and value:coder
"marks": [1,2,3,4],
"anotherdict": {"sattyam":"thakur"}
}

# print(myDict["sattyam"])
# print(myDict["fast"])
# myDict["marks"]=[99,87,56,45]                        # you can change the values easily
# print(myDict["marks"])
# print(myDict["anotherdict"]["sattyam"])
a =list(myDict.keys())   #this will return the keys
a =list(myDict.items())  #this will return the keys and values.
a =myDict.update({"friend":"pawan",00000:99999})
a = myDict.get("sattyam") #this will return the value of sattyam
print(a)
