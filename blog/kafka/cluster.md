2*n+1

```console
initLimit=10
syncLimit=5
server.1=172.16.70.129:2888:3888
server.2=172.16.70.130:2888:3888
server.3=172.16.70.131:2888:3888
```
2888:
3888:

```console
dataDir=/tmp/zookeeper
```

```console
cd /tmp/zookeeper
vim myid
cat myid
===>>>1
```

server.id:

```console
broker.id=1
zookeeper.connect=172.16.70.129:2181,172.16.70.130:2181,172.16.70.131:2181
```