# day 58 main File
class person:
    def __init__(self,n,o) -> None:
        print("I am a person")
        self.name = n
        self.occ = o

    def info (self):
        print(f"{self.name} is a {self.occ}")

# a = person()
# a.name = "Parth"
# a.occ = "Designer"
# print(a.name)
# a.info()
        
a = person("dhruvish", "Android devloper")
b = person("Parth" , "Designer")
a.info()
b.info()