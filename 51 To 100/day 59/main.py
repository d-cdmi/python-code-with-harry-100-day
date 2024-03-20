# day 59 main File
# Decorators function 
def greet (fx):
    def mfx (*args,**kwargs):
        print("Good Moring")
        fx(*args,**kwargs)
        print("Thank You for using")
    return mfx

@greet
def hello():
    print("Hello Word")
@greet
def add(a,b):
    print(a+b)

# hello()
# or
# greet(hello)()
# hello()

# greet(add)(10 ,20)
add(2,4)