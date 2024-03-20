# day 51 main File


# f = open('day 51/file.txt','w+')
# with open('day 51/file.txt',"r")as f:
#     print(type(f))
#     f.seek(0)
#     print(f.tell())                 #aapde kya point chhe te bakade
#     data = f.read(5)
#     print(data)


with open ('day 51/sample.txt','w') as f:
    f.write("hello Word")
    f.truncate(5)

with open ('day 51/sample.txt','r') as f:
    print(f.read())