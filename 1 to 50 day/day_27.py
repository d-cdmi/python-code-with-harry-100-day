print("Hello Welcome To KBC")
print("Only Three Qustion One Qustion $100 ")

print("-----------------------------------------")
# str1="a","b","c",'d',"e","f","g","h",'i',"j","k","l","m","n","o","p","q","r",'s',"t","u",'v',"w","x",'y',"z"
st="Who is Indian PM ?","What is the capital of India ?","What is the national bird of India","When was India is independence day?"
d=0
ans="narendra modi","delhi","peacock","droupadi murmu","august"
# ans=ans.lower()
# for a in st:
#     print(a)
#     ans1=input().lower()
#     for i in ans:
#         if ans1==i:
#             print("You Win $100")
#             d+=1
#         else:
#             break
#         print(d)


for a  in range(0,5):
    print(st[a])
    k=input()
    if k==ans[a]:
        print("yes")
        d+=1
    else:
        break





print("you Win for $",100*d)
        
    
