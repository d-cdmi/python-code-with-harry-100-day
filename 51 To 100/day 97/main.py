# day 97 main File
import threading
import time

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    return seconds

#sempal code
# func(4)
# func(2)
# func(1)

#user of threading
def ans():    
    time1 = time.perf_counter()
    t1 = threading.Thread(target=func,args=[4])
    t2 = threading.Thread(target=func,args=[2])
    t3 = threading.Thread(target=func,args=[1])

    t1.start()
    t2.start()
    t3.start()

    #My Work find for after program stop
    t1.join()
    t2.join()
    t3.join()

    time2 = time.perf_counter()
    print(time2-time1)