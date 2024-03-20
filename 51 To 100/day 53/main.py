# day 53 main File
#normal
# def cube (x):
#     return x*x*x
# print(cube(5))

# i = [1,2,5,7,6,3]
# # newl =[]
# # for item in i:
# #     newl.append(cube(item))
# # print(newl)

# #map
# newl = list(map(cube,i))
# print(newl)

#filter

l =[5,4,3,1,58,8,6,2]

def filter_fun(x):
    return x>5

newli = list(filter(filter_fun,l))
print(newli)

