Elasticsearch 入门
====================

Elasticsearch 是一个实时的分布式搜索分析引擎， 它能让你以一个之前从未有过的速度和规模，去探索你的数据。 它被用作全文检索、结构化搜索、分析以及这三个功能的组合

Elasticsearch 是一个开源的搜索引擎，建立在一个全文搜索引擎库 Apache Lucene™ 基础之上。 Lucene 可以说是当下最先进、高性能、全功能的搜索引擎库--无论是开源还是私有

但是 Lucene 仅仅只是一个库。为了充分发挥其功能，你需要使用 Java 并将 Lucene 直接集成到应用程序中。 更糟糕的是，您可能需要获得信息检索学位才能了解其工作原理。Lucene 非常复杂

Elasticsearch 也是使用 Java 编写的，它的内部使用 Lucene 做索引与搜索，但是它的目的是使全文检索变得简单， 通过隐藏 Lucene 的复杂性，取而代之的提供一套简单一致的 RESTful API

和 Elasticsearch 交互
-----

和 Elasticsearch 的交互方式取决于 你是否使用 Java

## Java API

如果你正在使用 Java，在代码中你可以使用 Elasticsearch 内置的两个客户端：

### 节点客户端（Node client）

节点客户端作为一个非数据节点加入到本地集群中。换句话说，它本身不保存任何数据，但是它知道数据在集群中的哪个节点中，并且可以把请求转发到正确的节点。

### 传输客户端（Transport client）

轻量级的传输客户端可以将请求发送到远程集群。它本身不加入集群，但是它可以将请求转发到集群中的一个节点上。

> Obtaining an elasticsearch Client is simple. The most common way to get a client is by creating a TransportClient that connects to a cluster.

两个 Java 客户端都是通过 9300 端口并使用本地 Elasticsearch 传输 协议和集群交互。集群中的节点通过端口 9300 彼此通信。如果这个端口没有打开，节点将无法形成一个集群。

Java 客户端作为节点必须和 Elasticsearch 有相同的 主要 版本；否则，它们之间将无法互相理解。

> The client must have the same major version (e.g. 2.x, or 5.x) as the nodes in the cluster. Clients may connect to clusters which have a different minor version (e.g. 2.3.x) but it is possible that new functionality may not be supported. Ideally, the client should have the same version as the cluster

## RESTful API with JSON over HTTP

所有其他语言可以使用 RESTful API 通过端口 9200 和 Elasticsearch 进行通信，你可以用你最喜爱的 web 客户端访问 Elasticsearch 。事实上，正如你所看到的，你甚至可以使用 curl 命令来和 Elasticsearch 交互。

一个 Elasticsearch 请求和任何 HTTP 请求一样由若干相同的部件组成：

```java
curl -X<VERB> '<PROTOCOL>://<HOST>:<PORT>/<PATH>?<QUERY_STRING>' -d '<BODY>'
```
* VERB  适当的HTTP方法或谓词:GET,POST,PUT,HEAD,DELETE

* PROTOCOL  http 或者 https

* HOST  Elasticsearch 集群中任意节点的主机名，或者用 localhost 代表本地机器上的节点

* PORT  运行 Elasticsearch HTTP 服务的端口号，默认是 9200

* PATH  API 的终端路径（例如 _count 将返回集群中文档数量）。Path 可能包含多个组件，例如：_cluster/stats 和 _nodes/stats/jvm

* QUERY_STRING  任意可选的查询字符串参数 (例如 ?pretty 将格式化地输出 JSON 返回值，使其更容易阅读)

* BODY  一个 JSON 格式的请求体 (如果请求需要的话)

Elasticsearch 安装
----

## 官方安装

安装 Elasticsearch 之前，你需要先安装一个较新的版本的 Java

之后，你可以从 elastic 的官网 elastic.co/downloads/elasticsearch 获取最新版本的 Elasticsearch

当你解压好了归档文件之后，Elasticsearch 已经准备好运行了

```java
cd elasticsearch-<version>
./bin/elasticsearch
```

* 如果你想把 Elasticsearch 作为一个守护进程在后台运行，那么可以在后面添加参数 -d

启动成功后可以打开浏览器访问9200端口测试是否启动成功

```json
http://localhost:9200
{
  "name" : "JJLUE6c",
  "cluster_name" : "elasticsearch",
  "cluster_uuid" : "HPXvtjhcRkmEOK1PDKlAmQ",
  "version" : {
    "number" : "5.6.7",
    "build_hash" : "4669214",
    "build_date" : "2018-01-25T21:14:50.776Z",
    "build_snapshot" : false,
    "lucene_version" : "6.6.1"
  },
  "tagline" : "You Know, for Search"
}
```

## docker安装

你可以直接前往Docker hub搜索elasticsearch

### 拉取镜像

目前最新版本的镜像是5.6.7

```java
docker pull elasticsearch:5.6.7
```

> Note: since 5.0, Elasticsearch only listens on localhost by default on both http and transport, so this image sets http.host to 0.0.0.0 (given that localhost is not terribly useful in the Docker context).

> As a result, this image does not support clustering out of the box and extra configuration must be set in order to support it.

> One example of adding clustering support is to pass the configuration on the docker run:
>```java
>$ docker run -d --name elas elasticsearch -Etransport.host=0.0.0.0 -Ediscovery.zen.minimum_master_nodes=1
>```