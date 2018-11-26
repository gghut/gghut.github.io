Elasticsearch 入门
====================

Elasticsearch 是一个实时的分布式搜索分析引擎， 它能让你以一个之前从未有过的速度和规模，去探索你的数据。 它被用作全文检索、结构化搜索、分析以及这三个功能的组合

Elasticsearch 是一个开源的搜索引擎，建立在一个全文搜索引擎库 Apache Lucene™ 基础之上。 Lucene 可以说是当下最先进、高性能、全功能的搜索引擎库--无论是开源还是私有

但是 Lucene 仅仅只是一个库。为了充分发挥其功能，你需要使用 Java 并将 Lucene 直接集成到应用程序中。 更糟糕的是，您可能需要获得信息检索学位才能了解其工作原理。Lucene 非常复杂

Elasticsearch 也是使用 Java 编写的，它的内部使用 Lucene 做索引与搜索，但是它的目的是使全文检索变得简单， 通过隐藏 Lucene 的复杂性，取而代之的提供一套简单一致的 RESTful API

面向文档
-----

也许有一天你想把这些对象存储在数据库中。使用关系型数据库的行和列存储，这相当于是把一个表现力丰富的对象挤压到一个非常大的电子表格中：你必须将这个对象扁平化来适应表结构--通常一个字段>对应一列--而且又不得不在每次查询时重新构造对象。

Elasticsearch 是 面向文档 的，意味着它存储整个对象或 文档_。Elasticsearch 不仅存储文档，而且 _索引 每个文档的内容使之可以被检索。在 Elasticsearch 中，你 对文档进行索引、检索、排序和过滤--而不是对行列数据。这是一种完全不同的思考数据的方式，也是 Elasticsearch 能支持复杂全文检索的原因。

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

Elasticsearch JAVA API
----

## Transport Client

```java
// on startup

TransportClient client = new PreBuiltTransportClient(Settings.EMPTY)
        .addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("host1"), 9300))
        .addTransportAddress(new InetSocketTransportAddress(InetAddress.getByName("host2"), 9300));

// on shutdown

client.close();
```

```java
Settings settings = Settings.builder()
        .put("cluster.name", "myClusterName").build();
TransportClient client = new PreBuiltTransportClient(settings);
//Add transport addresses and do something with the client...
```
* client.transport.sniff    enable sniffing

* client.transport.ignore_cluster_name  Set to true to ignore cluster name validation of connected nodes. (since 0.19.4)

* client.transport.ping_timeout The time to wait for a ping response from a node. Defaults to 5s

* client.transport.nodes_sampler_interval   How often to sample / ping the nodes listed and connected. Defaults to 5s

## 索引

存储数据到 Elasticsearch 的行为叫做索引，但在索引一个文档之前，需要确定将文档存储在哪里。

一个 Elasticsearch 集群可以包含多个索引，相应的每个索引可以包含多个类型。这些不同的类型存储着多个文档 ，每个文档又有多个属性 。

索引（名词）：

如前所述，一个 索引 类似于传统关系数据库中的一个 数据库 ，是一个存储关系型文档的地方。 索引 (index) 的复数词为 indices 或 indexes

索引（动词）：

索引一个文档 就是存储一个文档到一个 索引 （名词）中以便它可以被检索和查询到。这非常类似于 SQL 语句中的 INSERT 关键词，除了文档已存在时新文档会替换旧文档情况之外。

指定ID

```java
IndexResponse response = client.prepareIndex("twitter", "tweet", "1")
        .setSource(json)
        .get();
```
自动生成ID

```java
IndexResponse response = client.prepareIndex("twitter", "tweet")
        .setSource(json)
        .get();
```

## 检索

在 Elasticsearch 中很简单。简单地执行 一个 HTTP GET 请求并指定文档的地址——索引库、类型和ID,相当于SQL的SELECT

```java
GetResponse response = client.prepareGet("twitter", "tweet", "1").get();
```

在RESTFul API中:

* PUT   /twitter/tweet/1 索引数据

* GET   /twitter/tweet/1 检索数据

* DELETE   /twitter/tweet/1 删除数据

* HEAD   /twitter/tweet/1 查看数据是否存在

综上:可以猜测删除文档的API为

```java
DeleteResponse response = client.prepareDelete("twitter", "tweet", "1").get();
```

## 更新

更新文档

```java
client.prepareUpdate("twitter", "tweet", "1")
        .setDoc(json)
        .get();
```

更新插入文档

```java
IndexRequest indexRequest = new IndexRequest("index", "type", "1")
        .source(json);
UpdateRequest updateRequest = new UpdateRequest("index", "type", "1")
        .doc(json)
        .upsert(indexRequest);              
client.update(updateRequest).get();
```

## 搜索

```java
SearchResponse response = client.prepareSearch("index1", "index2")
        .setTypes("type1", "type2")
        .get();
```

### 精确值查找

当进行精确值查找时， 我们会使用过滤器（filters）。过滤器很重要，因为它们执行速度非常快，不会计算相关度（直接跳过了整个评分阶段）而且很容易被缓存

term查询:最为常用查询， 可以用它处理数字（numbers）、布尔值（Booleans）、日期（dates）以及文本（text）。

```java
SearchResponse response = client.prepareSearch("index1", "index2")
        .setTypes("type1", "type2")
        .setQuery(QueryBuilders.termQuery("字段", "值"))
        .get();
```

### 范围

```java
SearchResponse response = client.prepareSearch("index1", "index2")
        .setTypes("type1", "type2")
        .setPostFilter(QueryBuilders.rangeQuery("age").from(12).to(18))
        .get();
```

### 匹配

```java
SearchResponse response = client.prepareSearch("index1", "index2")
        .setTypes("type1", "type2")
        .setQuery(QueryBuilders.queryStringQuery(key))
        .get();
```