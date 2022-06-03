# Modern Data Center Systems - Distributed Shared Memory Demo

####⚠️ You need Docker to run this demo

✍🏻 Run writer:
```
docker build -f Dockerfile.writer --network host -t writer .
docker run --rm --name writer -v /dev/shm:/dev/shm -it writer
```

👓 Run reader:
```
docker build -f Dockerfile.writer --network host -t writer .
docker run --rm --name writer -v /dev/shm:/dev/shm -it writer
```

####Always start writer before reader!

🌍 Run synchroniser (not implemented yet):
```
# docker build -f Dockerfile.synchroniser --network host -t synchroniser .
# docker run --rm --name synchroniser -v /dev/shm:/dev/shm -it synchroniser
```