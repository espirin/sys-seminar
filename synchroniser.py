import os
import time

import requests as requests
from requests import RequestException

from config import SHM_NAME, SYNCHRONISATION_SERVER_ADDRESS, SYNCHRONISER_UPDATE_DELAY

last_shm = ""
shm_path = os.path.join("/dev/shm/", SHM_NAME)

while True:
    update_shm = False

    if os.path.exists(shm_path):
        # Read shared memory file
        with open(shm_path, "rb") as f:
            shm = f.read().decode('utf-8')

        # If it has changes, post them to the synchronisation server
        if shm != last_shm:
            try:
                requests.post(SYNCHRONISATION_SERVER_ADDRESS, json={
                    "shm": shm
                })
            except RequestException:
                print("Couldn't reach server or server error")
            else:
                last_shm = shm
        # If not, pull updates from the synchronisation server
        else:
            update_shm = True
    else:
        update_shm = True

    if update_shm:
        # Pull updates from the synchronisation server
        try:
            new_shm = requests.get(SYNCHRONISATION_SERVER_ADDRESS).json()['shm']
        except RequestException:
            print("Couldn't reach server or server error")
        else:
            # If there are changes on the server, update local shared memory
            if new_shm != last_shm:
                with open(shm_path, "wb") as f:
                    f.write(new_shm.encode('utf-8'))
                last_shm = new_shm

    time.sleep(SYNCHRONISER_UPDATE_DELAY)
