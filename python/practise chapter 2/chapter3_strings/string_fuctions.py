story = "once upon a time there was a engineer named sattyam who is learning python"

# STRING FUNCTIONS
#1. len function()
print(len(story))                # returns characters


#2. string.endswith
print(story.endswith("python"))   # returns true and false
print(story.endswith("upon"))


#3. string.count()
print(story.count("e"))           # counts character
print(story.count("a"))           # counts string also

#4. string.capatilise()
print(story.capitalize())         # used to capatalise the string

#5.string.find()
print(story.find("upon"))         # used to find index place

#6.string.replace()
print(story.replace("sattyam","sattu bhai"))         #replaces old word to new word

