```console
listeners=PLAINTEXT://0.0.0.0:9092
advertised.listeners=PLAINTEXT://172.16.70.129:9092
advertised.host.name=centos-1
```

```console
bin/zookeeper-server-start.sh config/zookeeper.properties
```

```console
bin/kafka-server-start.sh config/server.properties
```

```console
bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test
```

```console
bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test
```