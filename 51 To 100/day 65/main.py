# day 65 main File
class math:
    def __init__(self,num) -> None:
        self.num = num

    def addtonum(self,n):
        self.num = self.num +n
    @staticmethod
    def add(a,b):
        return a+b

a = math(5)
print(a.num)
a.addtonum(6)
print(a.num)

print(a.add(7,2))