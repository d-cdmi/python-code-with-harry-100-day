# day 57 main File

class person:
    name = 'Dhruvish'
    hobby = "cricket"
    networth = 24
    def info(self):
        print(f"{self.name} is hobby {self.hobby}")

a = person()

a.name = "ram"
print(a.name)
a.info()