# ques. write a program using function to find the greatest number using function?

def greatest(num1,num2,num3):
    if (num1>num2):
        return num1
    else:
            return num2
    if (num1>num3):
        return num1
    else:
            return num3
    if (num2>num3):
        return num2
    else:
            return num3
        

m = greatest(23,45,34)
print("the value of greatest number is " + str(m))        
