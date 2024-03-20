import os

path = "day 68/ram/"
# newex = str(input("Enter of New Exiation:\n"))
def renamdfin(newex):
    cont =0
    for i in os.listdir(path):
        sour = path + i
        os.rename(sour,path+str(cont)+newex)
        cont+=1
renamdfin(".png")