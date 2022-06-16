# Modern Data Center Systems Seminar - OpenWhisk DSM Demo

![example workflow](https://github.com/espirin/sys-seminar/actions/workflows/pylint.yml/badge.svg)

**⚠️ You need Docker and [our OpenWhisk fork](https://github.com/espirin/openwhisk-shm) to run this demo**

**❌️ OSX/Windows are not supported, run on x86 Linux**

## Demo Setup

<img width="750" alt="system_diagram" src="https://user-images.githubusercontent.com/71665653/174112743-845464b1-e297-4162-960b-543a02f13b70.png">


**Machine 1:**
- synchroniser
- writer (in OpenWhisk)

**Machine 2:**
- synchroniser
- reader (in OpenWhisk)

**Synchronisation server (you can use http://85.214.75.108:5000):**
- synchronisation server (Flask)

## Demo video
[![Demo video](https://i.ytimg.com/vi/UPCG7kJX1Oc/maxresdefault.jpg)](https://www.youtube.com/watch?v=UPCG7kJX1Oc)

## OpenWhisk setup
Install and run our OpenWhisk fork
```
git clone https://github.com/espirin/openwhisk-shm
cd openwhisk-shm
./gradlew core:standalone:bootRun
```
Install WSK (OpenWhisk CLI). Then unzip it and add wsk to your $PATH.
```
wget https://github.com/apache/openwhisk-cli/releases
```

Create OpenWhisk actions
```
wsk action create reader --docker nitrotube/python39_runtime reader.py
wsk action create writer --docker nitrotube/python39_runtime writer.py 
```

## How to run
##### 🌍 Synchroniser:
```
docker build -f Dockerfile.synchroniser --network host -t synchroniser .
docker run --rm --name synchroniser -v /dev/shm:/dev/shm -it --network host synchroniser
```

##### ✍🏻 Writer:
```
wsk action invoke --result writer --param seconds 10
```

##### 👓 Reader:
```
wsk action invoke --result reader --param seconds 10
```

Preferred starting order: writer, synchroniser, reader. 

##### 🖥 Synchronisation server:

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

👨‍🎓 2022 TUM - *Modern Data Center Systems Seminar*
