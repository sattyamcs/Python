# can you change the self parameter inside a class to something else(say"sattyam"). try changing self to 
# "slf" or "sattyam" and see the effects?

class Sample:
    def __init__(slf,name):
        slf.name= name

obj = Sample("sattyam")
print(obj.name)


#yes we can change the self parameter, it works but due to understanding of other programmers we are not doing this.
