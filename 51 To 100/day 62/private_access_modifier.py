class Employee:
    def __init__(self) -> None:
        self.__name = "dhruvish"
        self.__age = 18

a = Employee()
# print(a.__name) #can't be accessed directly
print(a._Employee__age)  #can be access first class name and after object name

print(a.__dir__())
