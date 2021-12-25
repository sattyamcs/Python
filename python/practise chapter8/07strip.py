# write a python function to removes a given word from a string and strip it at the same time
def remove_split(string,word):
    newStr = string.replace(word," ")
    return newStr.strip()

this = "          sattyam is a good developer"
n = remove_split(this,"sattyam")
print(n)
# print(this.strip())             #this function help us to remove extra spaces


