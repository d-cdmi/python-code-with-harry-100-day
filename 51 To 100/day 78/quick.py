class animal:
    def __init__(self,name) -> None:
        self.name = name
    def show(self):
        print(f"Show Detail is {self.name}")

class cat (animal):
    def __init__(self,name) -> None:
        self.name = name
    def show(self):
        print(f"Show Detail is {self.name} second")
        

a = cat("Ram")
a.show()        