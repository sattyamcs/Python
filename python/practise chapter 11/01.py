# create a class c2d vector and use it to create another class representing a 3d vector?

class C2Dvec:
    def __init__(self,i,j):
        self.icap = i
        self.jcap = j
    def __str__(self):
        return f"{self.icap}i + {self.jcap}j"


class C3Dvec(C2Dvec):
    def __init__(self,i,j,k):
        super().__init__(i,j,)
        self.kcap = k

    def __str__(self):
        return f"{self.icap}i + {self.jcap}j+ {self.kcap}"


v2d = C2Dvec(1,2)
v3d = C3Dvec(1,2,3)
print(v3d)

    