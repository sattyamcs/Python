# write a program to read the text from a given file '
# poem.txt' find out whether it contains the word twinkle?

f = open('poem.txt')
t = f.read()
if "twinkle" in t:
    print("twinkle is preasent")
else:
    print("twinkle is not presnt")

f.close()
