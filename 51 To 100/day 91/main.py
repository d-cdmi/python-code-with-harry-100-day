# day 91 main File
def my_genrator():
    for i in range(5000):
        yield i

gen = my_genrator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for j in gen:
    print(j)