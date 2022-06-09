import os
import time

import requests
from requests import RequestException

from config import SYNCHRONISATION_SERVER_URL, SYNCHRONISER_UPDATE_DELAY

LAST_SHM = b""
SHM_PATH = "/dev/shm/sys_seminar_shm"

while True:
    UPDATE_SHM = False

    if os.path.exists(SHM_PATH):
        # Read shared memory file
        with open(SHM_PATH, "rb") as f:
            shm = f.read()

        # If it has changes, post them to the synchronisation server
        if shm != LAST_SHM:
            try:
                requests.post(SYNCHRONISATION_SERVER_URL, data=shm)
            except RequestException as e:
                print("Couldn't reach server or server error")
                print(e)
            else:
                LAST_SHM = shm
                print("Pushed shared memory update to server")
        # If not, pull updates from the synchronisation server
        else:
            UPDATE_SHM = True
    else:
        UPDATE_SHM = True

    if UPDATE_SHM:
        # Pull updates from the synchronisation server
        try:
            new_shm = requests.get(SYNCHRONISATION_SERVER_URL).content
        except RequestException as e:
            print("Couldn't reach server or server error")
            print(e)
        else:
            # If there are changes on the server, update local shared memory
            if new_shm != LAST_SHM:
                with open(SHM_PATH, "wb") as f:
                    f.write(new_shm)
                LAST_SHM = new_shm
                print("Updated shared memory from server")

    time.sleep(SYNCHRONISER_UPDATE_DELAY)
