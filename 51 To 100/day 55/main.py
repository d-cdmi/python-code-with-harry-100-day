# day 55 main File
import random 

print(f'-------------------  Hello Welcome To My Game ------------------------')
t=int(input("Enter of Game Round : "))
i = 0
m = 0
c = 0
while True:
    while True:
        print(f'1:\tSenak\n2:\tWater\n3:\tGan')
        my = int(input("Enter of Number="))
        if my>=1 and my<=3:
            break
    comp = random.choice([1,2,3])
    print(f"computer choice is {comp}")

    if my == comp:
        # print("drow")
        c=c

    if my == 1:
        if comp==2:
            # print("Loss")
            c+=1
        elif comp == 3:
            # print("Win")
            m+=1

    elif my == 2:
        if comp==1:
            # print("Loss")
            c+=1
        elif comp == 3:
            # print("Win")
            m+=1

    elif my == 3:
        if comp==2:
            # print("Win")
            m+=1
        elif comp==1:
            # print("Loss")
            c+=1
    i+=1
    if t==i:
        break    

print(f"Computer Point Is {c} and Your Point Is {m}")    
if c==m:
    print("\n\nGame Is Drow")
elif c>m:
    print("\n\nYou Are Loss ")
else:
    print("\n\nYou Are Win")