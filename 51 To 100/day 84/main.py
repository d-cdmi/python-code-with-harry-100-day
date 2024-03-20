# day 84 main File
import time

def whieloop():
    i = 0
    while i<=50000:
        print(i)
        i = i+1

def forloop():
    for i in range(50000):
        print(i)

init = time.time()
whieloop()
t1 = time.time() - init
init = time.time()
forloop()
t2 = time.time() - init

print(f"{t1}\n\n{t2}")
