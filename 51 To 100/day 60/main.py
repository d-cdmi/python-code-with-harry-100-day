# day 60 main File
#Getters

class myclass:
    def __init__(self,value) -> None:
        self._value = value

    def  show(self):
        print(f'Value is {self._value}')
    
    @property
    def ten_value(self):
        return 10*self._value

#setter
    @ten_value.setter
    def ten_value(self,new_value):
        self._value = new_value/10


obj = myclass(10)
obj.ten_value = 67
print(obj.ten_value)
obj.show()

