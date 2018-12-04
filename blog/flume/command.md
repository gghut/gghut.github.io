
```console
vim conf/flume.conf
```

```console
agent.sources=s1
agent.sources.s1.type=exec
agent.sources.s1.command=cat /data/logs/nginx.log
agent.sources.s1.channels=c
agent.sources.s1.interceptors=i
agent.sources.s1.interceptors.i.type=timestamp
```

```console
agent.channels=c
agent.channels.c.type=memory
agent.channels.c.capacity=1000
agent.channels.c.transactionCapacity=100
```

```console
agent.sinks=k
agent.sinks.k.type=org.apache.flume.sink.kafka.KafkaSink
agent.sinks.k.channel=c
agent.sinks.k.kafka.bootstrap.servers=172.16.70.129:9092,172.16.70.130:9092,172.16.70.131:9092
agent.sinks.k.kafka.topic=nginx
agent.sinks.k.kafka.useFlumeEventFormat=true
agent.sinks.k.kafka.batchSize=20
agent.sinks.k.kafka.producer.requiredAcks=1
```

```sonsole
bin/flume-ng agent --conf conf --conf-file conf/flume.conf --name agent -Dflume.root.logger=INFO,console
```