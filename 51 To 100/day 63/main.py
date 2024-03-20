# day 63 main File
import random

user = int(input('1:\tSenak\n2:\tWater\n3:\tGan\n'))
comp = random.randint(1,3)

def check(user , comp):
    if user==comp:
        return 0
    elif comp==1 and user==2 or comp==2 and user==3 or comp==3 and user==1:
        return -1
    return 1
print(f'computer choice:{comp}\n user Choice :{user}')
ans= check(user,comp)

if(ans==1):
    print("Your are Wen")

if(ans==-1):
    print("Your are less")

if(ans==0):
    print("Your are drow")