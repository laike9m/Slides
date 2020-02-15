import concurrent.futures
import time
from concurrent.futures import ThreadPoolExecutor, FIRST_COMPLETED

def wait_n_seconds(n):
  time.sleep(n)
  
def wait_and_see_result(fs):
    time.sleep(1)
    result = concurrent.futures.wait(fs, return_when=FIRST_COMPLETED)
    print("done: ", result.done)
    print("not done: %s\n" % result.not_done)

with ThreadPoolExecutor(3) as e:
  f1 = e.submit(wait_n_seconds, 1)
  f2 = e.submit(wait_n_seconds, 2)
  f3 = e.submit(wait_n_seconds, 3)
  fs = [f1, f2, f3]
  wait_and_see_result(fs)
  wait_and_see_result(fs)
  wait_and_see_result(fs)
