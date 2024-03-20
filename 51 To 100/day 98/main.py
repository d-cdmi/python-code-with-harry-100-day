# day 98 main File
import multiprocessing
import requests
import concurrent.futures

def DownloadFile(url,name):
    print(f"Downlod Start {name}")
    response = requests.get(url)
    open (f"day 98/file/{name}.jpg","wb").write(response.content)
    print(f"Downlod End: {name}")

if __name__ == "__main__":
    url = "https://picsum.photos/2000/0000"
    # pros = []
    # for i in range(6):
    #     # DownloadFile(url,i)
    #     p = multiprocessing.Process(target=DownloadFile,args=[url,i])
    #     p.start()
    #     pros.append(p)
    # for i in pros:
    #     i.join()

    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(60)]
        l2 = [i for i in range(60)]
        results = executor.map(DownloadFile,l1,l2)
        for r in results:
            print(r)