# ques. write a program to find out whether a given post is talking about "sattyam" or not?

post = input("write a post\n")
name = str(post.find("sattyam"))

if  name in post:
    print("it presents")
else:
    print("not present")
