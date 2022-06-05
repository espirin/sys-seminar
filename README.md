# Modern Data Center Systems - Distributed Shared Memory Demo

**⚠️ You need Docker to run this demo**

**❌️ OSX/Windows are not supported, run on Linux**

###Demo Setup
**Machine 1:**
- synchroniser
- writer

**Machine 2:**
- synchroniser
- reader

**Synchronisation server (you can use http://85.214.75.108:5000):**
- synchronisation server

###How to run
🌍 Synchroniser:
```
docker build -f Dockerfile.synchroniser --network host -t synchroniser .
docker run --rm --name synchroniser -v /dev/shm:/dev/shm -it --network host synchroniser
```

✍🏻 Writer:
```
docker build -f Dockerfile.writer --network host -t writer .
docker run --rm --name writer -v /dev/shm:/dev/shm -it writer
```

👓 Reader:
```
docker build -f Dockerfile.reader --network host -t reader .
docker run --rm --name reader -v /dev/shm:/dev/shm -it reader
```

🖥 Synchronisation server:

There's already a **demo server** running at http://85.214.75.108:5000. You can use it for tests.

If you want to set up **your own server:**

Run synchronisation server in venv instead of Docker to avoid setting up Nginx. Replace */path/to/venv/bin/python* with path to your *venv/vin/python*.

Don't forget to change *SYNCHRONISATION_SERVER_URL* in config.py if you run your own synchronisation server.
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
sudo /path/to/venv/bin/python synchronisation_server.py
```
