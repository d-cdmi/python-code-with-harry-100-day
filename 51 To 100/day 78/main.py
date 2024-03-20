# day 78 main File
class stu:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id

    def showdet(self):
        print(f"Dhruvish Lathiya")

class hello(stu):
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id
        
    def showdet(self):
        print(f"second Name")

a = stu("dhruvish",420)
a.showdet()
b = hello("hello",740)
b.showdet()


