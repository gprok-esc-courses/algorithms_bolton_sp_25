import time 
import random

def counter(name):
    for i in range(10):
        print(name, i)
        time.sleep(random.randint(2, 5))


if __name__ == '__main__':
    callers = ['A', 'B', 'C', 'D', 'E']
    for caller in callers:
        counter(caller)