from copy import copy
from multiprocessing import shared_memory
from time import sleep

import numpy as np


def main(args):
    existing_shm = shared_memory.SharedMemory(name="sys_seminar_shm")
    c = np.ndarray((5,), dtype=np.int64, buffer=existing_shm.buf)

    print("Printing numpy array from shared memory...")
    local_copy = copy(list(c))
    for i in range(args.get("cycles", 300)):
        if list(c) != local_copy:
            print(c)
            local_copy = copy(list(c))
        sleep(0.1)

    return {"status": "done"}
