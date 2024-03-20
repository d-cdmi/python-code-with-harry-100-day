# day 77 main File
class Vector :
    def __init__(self,i,j,k) -> None:
        self.i =i
        self.j =j
        self.k =k
    def __str__(self) -> str:
        return f'{self.i}i+ {self.j}j+ {self.k}k'
    def __add__(self,x):
        return Vector(self.i+x.i,self.k+x.k,self.k+x.k)

v1 = Vector(5,8,6)
print(v1)

v2 = Vector(6,8,4)
print(v2)

print(v1+ v2)