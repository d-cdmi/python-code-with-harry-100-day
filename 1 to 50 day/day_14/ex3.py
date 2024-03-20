a=input("Enter of Zender= ")
b=int(input("Enter of Age= "))

if(a=='m'):
    if(b<18):
        print("You male and age is 18 below")
    else:
        print("You male and age is 18 to height")
elif(a=='F'):
    if(b<18):
        print("You gril and age is 18 below")
    else:
        print("You gril and age is 18 to height")
else:
    print("you are other")