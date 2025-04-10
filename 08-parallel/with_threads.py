import time 
import random
from threading import Thread

def counter(name):
    for i in range(10):
        print(name, i)
        time.sleep(random.randint(2, 5))


if __name__ == '__main__':
    callers = ['A', 'B', 'C', 'D', 'E']
    threads = []
    for caller in callers:
        th = Thread(target=counter, args=(caller,))
        threads.append(th)
        th.start()
    for th in threads:
        th.join()
    print("COMPLETED")

