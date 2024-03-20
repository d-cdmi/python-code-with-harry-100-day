# day 64 main 
class libr:
    i = 0
    def __init__(self,book) -> None:
        self.Book = book
        libr.i+=1

    def info(self):
        print(f'Name is {self.i} and Book Name {self.Book}')

a = libr("Ram")
a.info()