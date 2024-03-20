# reduce
from functools import reduce

num = [5,8,6,4,2]

def sum(x,y):
    return x+y

print(reduce(sum,num))