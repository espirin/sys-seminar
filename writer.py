from multiprocessing import shared_memory
from time import sleep

import numpy as np


def main(args):
    try:
        shm = shared_memory.SharedMemory(name="sys_seminar_shm")
        shm.unlink()
        shm.close()
    except (IndexError, ValueError, FileExistsError):
        pass

    start_array = np.array([1, 1, 2, 3, 5])
    shm = shared_memory.SharedMemory(create=True, size=start_array.nbytes, name="sys_seminar_shm")
    shared_memory_array = np.ndarray(start_array.shape, dtype=start_array.dtype, buffer=shm.buf)
    shared_memory_array[:] = start_array[:]

    print("Modifying numpy array in shared memory...")
    for _ in range(args.get("seconds", 10)):
        for i in range(len(shared_memory_array) - 1):
            shared_memory_array[i] = shared_memory_array[i + 1]
        shared_memory_array[-1] = shared_memory_array[-2] + shared_memory_array[-3]
        print(shared_memory_array)
        sleep(1)

    return {"status": "done"}
