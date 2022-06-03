from multiprocessing import shared_memory
from time import sleep

import numpy as np

from config import SHM_NAME

try:
    shm = shared_memory.SharedMemory(name=SHM_NAME)
    shm.unlink()
    shm.close()
except:
    pass

a = np.array([1, 1, 2, 3, 5])
shm = shared_memory.SharedMemory(create=True, size=a.nbytes, name=SHM_NAME)
b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
b[:] = a[:]

print("Modifying numpy array in shared memory...")
while True:
    for i in range(len(b) - 1):
        b[i] = b[i + 1]
    b[-1] = b[-2] + b[-3]
    print(b)
    sleep(1)
