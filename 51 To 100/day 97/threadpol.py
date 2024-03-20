from concurrent.futures import ThreadPoolExecutor
from main import func 
def demo():
    with ThreadPoolExecutor(max_workers=1) as executor:
        # future1 = executor.submit(func,4)
        # future2 = executor.submit(func,2)
        # future3 = executor.submit(func,1)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        l = [3,2,5,7]
        results = executor.map(func,l)
        for i in results:
            print(i)

demo()
