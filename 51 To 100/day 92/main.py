# day 92 main File
import functools as fo
import time
@fo.lru_cache(maxsize=None)
def fib(n):
    time.sleep(3)
    return n*5

print(fib(5))
print(fib(2))
print(fib(4))
print(fib(8))
print(fib(5))
print(fib(7))
print(fib(5))