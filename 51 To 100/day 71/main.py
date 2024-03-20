# day 71 main File
# dir
# x = (1,2,3,4)
# print(dir(x))
# print(x.__add__)

class pre:
    def __init__(self,name ,age) -> None:
        self.name = name
        self.age = age

p = pre("jon",30)
print(p.__dict__)
print(p.__dir__)

print(help(pre))