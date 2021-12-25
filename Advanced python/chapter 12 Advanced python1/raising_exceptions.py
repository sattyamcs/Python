def  increment (num):
    try:              
        return int(num)+1
    except:           # if we put some charcters it raise value error and display over it
        raise ValueError("this is incorrect")

a = increment("kk89") #it shows error and shows what you customised statement to show
print(a)