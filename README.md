# Modern Data Center Systems - Distributed Shared Memory Demo

**⚠️ You need Docker to run this demo**

**❌️ OSX ist not supported, run on Linux**

✍🏻 Run writer:
```
docker build -f Dockerfile.writer --network host -t writer .
docker run --rm --name writer -v /dev/shm:/dev/shm -it writer
```

👓 Run reader:
```
docker build -f Dockerfile.reader --network host -t reader .
docker run --rm --name reader -v /dev/shm:/dev/shm -it reader
```

**Always start writer before reader!**

🌍 Run synchroniser (not implemented yet):
```
docker build -f Dockerfile.synchroniser --network host -t synchroniser .
docker run --rm --name synchroniser -v /dev/shm:/dev/shm -it --network host synchroniser
```