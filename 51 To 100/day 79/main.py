# day 79 main File
class person:
    def __init__(self,name) -> None:
        self.name = name
    
    def show(self):
        print(f"The Name is {self.name}")
class dacnerr:
    def __init__(self,dance) -> None:
        self.name = dance
class max(person,dacnerr):
    def __init__(self,name,dance):
        self.name = name
        self.dance = dance

o = max("ram","Garba")
print(o.name)
print(o.dance)
o.show()        #class max(person,dacnerr):    aa ma je phelelu hoy te bakave\
print(max.mro())