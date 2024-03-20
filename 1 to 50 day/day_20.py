# def isc(num,st,end):
#     for i in range(st,end):
#         print(num,"X",i,"=",num*i)

# # table

# isc(9,0,11)

#palindrom number
def sum():
    pass
#CODE pachi lakhi shakay aanathi


def pali(num):
    sum=0
    te=num
    re=0
    while(num!=0):
        sum=int((sum*10 ) + (num%10))
        num=int(num/10)
    if(te==sum):
        print("Is palindrom Number")
    else:
        print("IS Non't palindrom Number")


pali(163)


