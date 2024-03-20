# day 75 main File
import os
files = os.listdir("day 75/Ram")
i = 1
for file in files:
    if file.endswith(".txt"):
        os.rename(f"day 75/Ram/{file}",f"day 75/Ram/{i}.py")
        i =i +1