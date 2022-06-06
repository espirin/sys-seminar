from multiprocessing import shared_memory
from time import sleep

import numpy as np


def main(args):
    try:
        shm = shared_memory.SharedMemory(name="sys_seminar_shm")
        shm.unlink()
        shm.close()
    except:
        pass

    a = np.array([1, 1, 2, 3, 5])
    shm = shared_memory.SharedMemory(create=True, size=a.nbytes, name="sys_seminar_shm")
    b = np.ndarray(a.shape, dtype=a.dtype, buffer=shm.buf)
    b[:] = a[:]

    print("Modifying numpy array in shared memory...")
    for _ in range(args.get("seconds", 10)):
        for i in range(len(b) - 1):
            b[i] = b[i + 1]
        b[-1] = b[-2] + b[-3]
        print(b)
        sleep(1)

    return {"status": "done"}
