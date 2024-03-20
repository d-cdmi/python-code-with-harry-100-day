# # Recursion
# #fac
# def fac(n):
#     if n==0 or n==1:
#         return 1
#     else:
#         return n * fac(n-1)
# fac(5)
# print(fac(5))

# f

# Python program to display the Fibonacci sequence

def recur_fibo(n):
    a=0
    b=1
   
    if n <= 1:
       return n
    else:
        c=a
        a=b
        b=c
        
        return(recur_fibo(c))

print( recur_fibo(10))

# check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))
