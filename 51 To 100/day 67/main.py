# day 67 main File
class library:
    def __init__(self) -> None:
        self.nobook = 0
        self.book = []
    
    def addbook(self,book):
        self.book.append(book)
        self.nobook = len(self.book)

    def showInfo(self):
        print(f"The lobrary has {self.nobook} books")

        for book in self.book:
            print(book)

l1 = library()
l1.addbook("dhruvish 1")
l1.addbook("dhruvish 2")
l1.addbook("dhruvish 3")
l1.addbook("dhruvish 4")

l1.showInfo( )