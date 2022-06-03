import os

from config import SHM_NAME

with open(os.path.join("/dev/shm/", SHM_NAME), "rb") as f:
    x = f.read()

print(x)
