# day 96 main File
import time
import asyncio
import requests
import requests


async def fun1():
    url = 'https://drive.google.com/file/d/17Gv5m3Ipzg2xZkbsbsj-qhqc6jCTNTif/view?usp=drive_link'
    r = requests.get(url, allow_redirects=True)
    open('google1.mp4', 'wb').write(r.content)
    print("fun 1")

async def fun2():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google2.ico', 'wb').write(r.content)
    print("fun 2")

async def fun3():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url, allow_redirects=True)
    open('google3.ico', 'wb').write(r.content)
    print("fun 3")
    return "dhruvish"

async def main():
    L = await asyncio.gather(
        fun1(),
        fun2(),
        fun3()
    )
    print(L)








    # task = asyncio.create_task(fun1())
    # await fun1() 
    # await fun2()
    # await fun3()

asyncio.run(main())