import os
import time

import requests as requests
from requests import RequestException

from config import SYNCHRONISATION_SERVER_URL, SYNCHRONISER_UPDATE_DELAY

last_shm = b""
shm_path = "/dev/shm/sys_seminar_shm"

while True:
    update_shm = False

    if os.path.exists(shm_path):
        # Read shared memory file
        with open(shm_path, "rb") as f:
            shm = f.read()

        # If it has changes, post them to the synchronisation server
        if shm != last_shm:
            try:
                requests.post(SYNCHRONISATION_SERVER_URL, data=shm)
            except RequestException as e:
                print("Couldn't reach server or server error")
                print(e)
            else:
                last_shm = shm
                print("Pushed shared memory update to server")
        # If not, pull updates from the synchronisation server
        else:
            update_shm = True
    else:
        update_shm = True

    if update_shm:
        # Pull updates from the synchronisation server
        try:
            new_shm = requests.get(SYNCHRONISATION_SERVER_URL).content
        except RequestException as e:
            print("Couldn't reach server or server error")
            print(e)
        else:
            # If there are changes on the server, update local shared memory
            if new_shm != last_shm:
                with open(shm_path, "wb") as f:
                    f.write(new_shm)
                last_shm = new_shm
                print("Updated shared memory from server")

    time.sleep(SYNCHRONISER_UPDATE_DELAY)
