import time

data = list(range(1_000_000))

start = time.time()
result = [x * 2 for x in data]
print(time.time() - start)

import sys

print(sys.path)

import numpy as np

arr = np.array(data)

start = time.time()
result = arr * 2
print(time.time() - start)
