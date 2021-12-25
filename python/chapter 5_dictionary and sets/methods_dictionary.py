myDict = { "fast": "a quick manner",               
"sattyam": "a coder",                              
"marks": [1,2,3,4],
"anotherdict": {"sattyam":"thakur"},
1:2

}
# DICTIONARY METHODS
print(list(myDict.keys()))               #it returns the keys item
print(list(myDict.values()))             #it returns values
print(list(myDict.items()))             #it returns keys,values of all contents

updatedict = {     
    "shivam":"friend",
    "divya":"friend",
    7888:999,
    "sattyam":"a engineer"                #it will update the last value for the same key
}
myDict.update(updatedict)                 #used to update the dict by adding more keys and values
print(myDict)

print(myDict.get("sattyam"))             #prints value associates with "sattyam"
print(myDict["sattyam"])                 #prints value associates with "sattyam"

# difference btwn .get and square[] bracket syntex

print(myDict.get("sattyam2"))        #returns none as the key sattyam is not present in dictionary
print(myDict["sattyam2"])           #throws error as sattyam2 is not present in dictionary



