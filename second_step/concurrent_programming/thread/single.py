from thread.test import *
import time

start_time = time.time()
for i in range(10):
    # count(1,1)
    io()
print("Single cpu:",time.time()-start_time)
