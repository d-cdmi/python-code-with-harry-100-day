# #reading file
# f = open ("myfile.txt","rb") #defult value r 
# # print(f)
# text =f.read()
# print(text)
# f.close()

# #writing a file
# f = open ("myfile2.txt","a")
# f.write("hello word \n")
# f.close()
# f = open ("myfile2.txt","r")
# text = f.read()
# print(text)



#with
with open("myfile.txt","a") as f:
    f.write("hey I am inside with ")