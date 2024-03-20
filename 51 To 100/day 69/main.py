# day 69 main File
# chane the class vaulue in @

class employee:
    company = "apple"
    def show(self):
        print(f"The name is {self.name} and company Name {self.company}")
    
    # @classmethod     #change the last number
    def changecompany(cls,Newcompany):
        cls.company = Newcompany

a = employee()
a.name = "Dhruvish"
a.show()
a.changecompany("Tasla")
a.show()
print(employee.company)
