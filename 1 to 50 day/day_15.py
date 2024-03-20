import time

# import time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
# # https://docs.python.org/3/library/time.html#time.strftime

# print(2+2)
# h=int(input("enter of a="))

h=int(time.strftime('%H'))

if(h<=12):
    print("good moring")
elif(h<=17):
    print("good afterver")
else:
    print("good niet")




# 5 to 12   good moring
# 12 to 6     good after
# 6 to 5      good ninght
    

# if(a<12)
# gm
# if()