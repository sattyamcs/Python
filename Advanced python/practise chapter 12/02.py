# write a program to print third  fifth and seventh element of a list using enumerate method?

list = ["sattyam",22,26,48.90,False,"jamura","sandeepa"]

for index ,item in enumerate(list):
    if index == 2 or index == 4 or index == 6:
        # print(index,item)
        print(f"The {index+1}rd element is {item}")
