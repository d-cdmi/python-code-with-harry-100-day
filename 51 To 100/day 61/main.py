# day 61 main File
class Emplo:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id

    def showdetail(self):
        print(f'The Name of Employee {self.id} is {self.name}')

class program(Emplo):
    def showprogramer(self):
        print(f"hey This is programer")
    

# a1=Emplo('dhruvish',520)
# a1.showdetail()

a2=program('dhruvish',520)
a2.showdetail()
a2.showprogramer()