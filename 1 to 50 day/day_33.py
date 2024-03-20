dic  ={
    5:"dhruvish",
    6:"shubam",
    9:"Raj",
    50:"Ronak"
}
# print(dic)
# print(dic[5])               #no hoy toerror
# print(dic.get(200))        #no hoy  to none


#multipal value accessing
print(dic.keys())
print(dic.values())

# for i in dic.keys():
#     print(dic[i])

for key,value in dic.items():
    print(f"key is {key} and Value is {value}")