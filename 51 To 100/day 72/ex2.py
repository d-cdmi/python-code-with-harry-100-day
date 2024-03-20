class employerr:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id

class programer(employerr):
    def __init__(self, name, id,lan) -> None:
        self.lan = lan
        super().__init__(name, id)
    
Dhruvish = employerr("Dhruvish",4852)
raj = programer("Vaj",852,"Python")
print(Dhruvish.name)
print(Dhruvish.id)
print(raj.name)
print(raj.id)
print(raj.lan)
