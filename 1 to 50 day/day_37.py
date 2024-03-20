def func1():
    try:
        i=[3,5,2,5]
        i=int(input("Enter of number="))
        print(i)
        return 1
    except:
        print("Error For function")
        return 0
    finally:
        print("This always exection")
    
x=func1()
print(x)