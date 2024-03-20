a=int(input("Enter of Number= "))
def num(a):
    match a:
        case 0:
            print("Is a Zero")
        case 1:
            print("Is a one")
        case 2:
            print("Is a two")
        case 3:
            print("Is a three")
        case _ if(a!=10):
            print("a Is not equl to 1o")
