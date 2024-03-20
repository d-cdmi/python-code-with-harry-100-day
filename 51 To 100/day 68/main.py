# day 68 main File
import os
import random

# Create a Folder and in folder create a 100 file
part = "day 75/Ram"
a = int(input(("Create a Folder Type \t\t 0: \nNot Create a Folder Type \t 1:\n")))
if(a==0):
    os.mkdir(part)
file = str(input("Enter of file Type :\n"))
part = part+"/"
for i in range(0,100):
    name = 0
    name = chr(random.randint(97 , 123))
    t=random.randint(1 ,10)
    for i2 in range(0,t):
        temp =chr(random.randint(97 , 123)) 
        name = str(name+temp)
    fileName = part+name+file
    with open (fileName,"w") as pd:
        pass

print(f"Findy Create a {i} File")