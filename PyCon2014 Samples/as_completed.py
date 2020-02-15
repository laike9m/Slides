import concurrent.futures
import time
from concurrent.futures import ThreadPoolExecutor

def wait_n_seconds(n):
  time.sleep(n)
  return n

with ThreadPoolExecutor(3) as e:
  f1 = e.submit(wait_n_seconds, 1)
  f2 = e.submit(wait_n_seconds, 2)
  f3 = e.submit(wait_n_seconds, 3)
  fs = [f1, f2, f3]
  for f in concurrent.futures.as_completed(fs):
      print("done: %s, result: %d" % (f.done(), f.result()))
