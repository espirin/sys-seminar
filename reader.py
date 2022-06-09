from copy import copy
from multiprocessing import shared_memory
from time import sleep

import numpy as np


def main(args):
    existing_shm = shared_memory.SharedMemory(name="sys_seminar_shm")
    shared_memory_array = np.ndarray((5,), dtype=np.int64, buffer=existing_shm.buf)

    print("Printing numpy array from shared memory...")
    local_copy = copy(list(shared_memory_array))
    for _ in range(args.get("seconds", 10) * 10):
        if list(shared_memory_array) != local_copy:
            print(shared_memory_array)
            local_copy = copy(list(shared_memory_array))
        sleep(0.1)

    return {"status": "done"}
