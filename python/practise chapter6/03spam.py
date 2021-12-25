# ques. a spam comment is defined as a text containing following keywords
"make a lot of money", "buy now","subscribe this", "clik this"
# write a program to delete these spams


text = input("enter the text\n")

if("make a lot of money" in text):
    spam = True
elif("buy now" in text):
    spam = True
elif("subscribe this" in text):
    spam = True
elif("clik this" in text):
    spam = True
else:
    spam = False

if (spam):
    print("this text is spam")
else:
    print("this text is not spam")
