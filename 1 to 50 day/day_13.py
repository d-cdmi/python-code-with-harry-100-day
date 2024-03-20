# string function

a="dhruvish"
print(len(a))
print(a.upper())
print(a.lower())


str="dhRuvish lathiya shubham ..........!"
print(str.rstrip('!'))

print(str.replace("dhruvish" , "shubham"))

print(str.split(" "))

print(str.capitalize())

str1="dhruvish"
print(len(str1))
print(len(str1.center(41)))

b="anbjisntlsda;rinsdfn"
print(b.count('a'))

print(b.endswith('n'))

c="welcome the my work password"

print(c.endswith("come",3,7))

print(c.find('dhruvihs'))   # find the value of returen of index number and no avablie the program is return of -1

# print(c.index('dhruvihs'))        error false

d="wecome"
print(d.isalnum())
d="         "
print(d.isalpha())

print(d.islower())

print(d.isprintable())

print(d.isspace())
d="Hello word"
print(d.istitle())

d="HELLO WORK"

print(d.isupper())

d="Welcome Goolge"

print(d.startswith("wel"))

print(d.swapcase())

d="hello my name is dhruvish"

print(d.title())

