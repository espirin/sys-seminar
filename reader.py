from copy import copy
from multiprocessing import shared_memory
from time import sleep

import numpy as np

from config import SHM_NAME

existing_shm = shared_memory.SharedMemory(name=SHM_NAME)
c = np.ndarray((5,), dtype=np.int64, buffer=existing_shm.buf)

print("Printing numpy array from shared memory...")
local_copy = copy(list(c))
while True:
    if list(c) != local_copy:
        print(c)
        local_copy = copy(list(c))
    sleep(0.1)
