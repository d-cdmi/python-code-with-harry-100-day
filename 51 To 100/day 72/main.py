# day 72 main File

class parentClass:
    def parent_method(self):
        print("This is a Parent Method")

class childClass (parentClass):
    def parent_method(self):
        print("Dhruvish")
        super().parent_method()
    def child_method(self):
        print("This Is a child Method")
        super().parent_method()

a = childClass()
a.child_method()