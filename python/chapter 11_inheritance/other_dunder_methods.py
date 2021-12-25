class Number:
    def __init__(self,num):
        self.num = num

    def __add__(self,num2):
        print("lets add")
        return self.num + num2.num


    def __mul__(self,num2):
        print("lets multiply")
        return self.num * num2.num

    def __str__(self):
        return f"decimal number :{self.num}"

    def __len__(self):
        return 1


n = Number(28)
print(n)
print(len(n))