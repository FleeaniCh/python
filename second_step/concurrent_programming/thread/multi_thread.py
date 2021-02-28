from thread.test import *
from threading import Thread
import time

jobs = []
tm = time.time()
if __name__ == '__main__':

    for i in range(10):
        p = Thread(target=io)
        jobs.append(p)
        p.start()

    for i in jobs:
        i.join()
    print("Thead cpu:",time.time()-tm)