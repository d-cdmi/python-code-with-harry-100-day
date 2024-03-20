#readline() Method
# f = open("myfile.txt",'r')
# while True:
#     line = f.readline()
#     print(line)
#     if not line:
#         break

#example 
# i=0
# f = open("myfile.txt",'r')
# while True:
#     i=i + 1
#     line = f.readline()
#     if not line:
#         break
#     m0 = int(line.split(',')[0])
#     m1 = int(line.split(',')[1])
#     m2 = int(line.split(',')[2])

#     print(f'Mark of math = {m0}')
#     print(f'Mark of math = {m1}')
#     print(f'Mark of math = {m2}')

#     print(line)


#writeline()method

f = open('myfile2.txt','w')
lines = ["line 1\n","line2 \n",'line 3 \n']
f.writelines(lines)
f.close()







