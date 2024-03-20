# day 66 main File
class emloyee:
    compiName = "Lathiya"
    NumOfemp = 0
    def __init__(self,name) -> None:
        self.name = name
        self.raise_aumont = 0.45
        emloyee.NumOfemp+=1

    def showdetail(self):
        print(f"The name of The Employee is {self.name} and the raise amount in {self.compiName} is {self.raise_aumont}  and employee is {self.NumOfemp}")
    
# emloyee.showdetail(emp1)
emp1 = emloyee("dhruvish")
emp1.raise_aumont = 5
emp1.compiName = "google"
emp1.showdetail()

emloyee.compiName = "apple"

emp2 = emloyee("Raj")
emp2.compiName = "amezon"
emp2.showdetail()
