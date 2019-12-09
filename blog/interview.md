面试
===

数据结构
===

## HashMap

由数组+链表、红黑树实现，由key的hash码无符号右移16位后与原hash码异或得到的值取摸后确定该k-v结构在数组中的存储位置。

数组中每个元素为一个链表/红黑树的头节点。当容量小于64时，出现链表长度超过8优先采取扩容数组长度，当容量超过64之后链表长度超过8将链表改为红黑树，数组每次扩容将原数组中数据复制到新的数组中(重新hash)，容量为原来的两倍，当使用量达到最大量的75%也会触发扩容。

## HashTable

继承与Dictionary，实现了Map，Cloneable，Serializable接口。方法是同步的，他是线程安全的，kv不能为null，key无序

### HashMap与HashTable的区别

* 父类不同，hashMap继承自AbstractMap，hashTable继承自Dictionary
* HashMap线程不安全，HashTable使用Synchronized，线程安全
* HashMap只包含containsKey以及containsValue，HashTable包含contains（同containsKey）、containsKey，containsValue
* HashMap允许可以一个key为null，多个value为null，HashTable的key-value一个都不允许为null
* HashTable保留了Enumeration遍历方式
* HashTalbe直接使用hashCode取摸，HashMap运用hashCode的高16位与低16位做异或运算再取摸
* HashTable在不指定容量的默认值为11，扩容为old×2+1，HashMap为16，扩容为2×old

算法
===

多线程
===

### Synchronized与ReentrantLock的区别

* ReentrantLock可以设置为公平锁，对象锁
* 两者都可重入
* 可以响应中断
* 可选择性中断

### Synchronized和Volatile的区别

* volatile是线程同步的轻量级实现，性能优于Synchronized
* volatile只能修饰变量，而Synchronized可以修饰方法和代码块
* 多线程访问volatile不会发生阻塞，访问Synchronized会
* volatile可以保证数据的可见性，但是不能保证数据的原子性，Synchronized既可以保证原子性，又可以保证可见性
* volatile主要保证多个线程间的可见性，Synchronized主要保证多个线程间的同步性

关于指令重排的Happens-Beefore原则：<br>
* 程序顺序性原则：一个线程内保证语意的串行性
* volatile规则：volatile变量的写先于读，保证了volatile变量的可见性
* 锁规则：解锁必然发送在随后的加锁之前（必须要先解锁才能获得锁）
* 传递性：A先于B，B先于C，那么A必然先于C
* 线程的start方法先于它的每一个动作
* 线程所有的操作先于join
* 线程的中断先于被中断的代码
* 对象的构造函数的执行、结束先于finalize()

## 线程池

### 线程的状态

```java
public enum State{
    NEW,//新建，还未执行
    RUNNABLE,//开始执行，调用start()之后
    BLOCKED,//遇到synchronized，lock且没有取得相应的锁
    WAITING,//调用wait()，join()
    TIMED_WAITING,//调用wait(long timeoutMillis),sleep()
    TERMINATED;//执行结束
}
```

### 线程池参数

* corePoolSize 指定线程池中的线程数量
* maxinumPoolSize 指定线程池中的最大线程数量
* keepAliveTime 当线程池中线程数量操作corePoolSize时，多余的空闲线程的存活时间
* unit keepAliveTime的单位
* workQueue 任务队列，被提交但尚未被执行的任务
* threadFactory 线程工厂，用于创建线程，一般使用默认
* handler 拒绝策略，当超过workQueue最大容量时采用拒绝策略

### 关于线程数量

当线程数量小于corePoolSize时，直接创建线程处理任务（创建线程需要使用全局锁），当线程数量超过corePoolSize时，新的任务提交到workQueue，当workQueue满时继续创建线程执行任务（需要全局锁），当线程数量超过maxinumPoolSize时，执行拒绝策略

### 线程池的拒绝策略

* AbortPolicy 直接抛出异常，阻止系统正常工作
* CallerRunsPolicy 由调用者执行当前任务
* DiscardOldestPolicy 丢弃任务队列中最老的一个请求（即将执行的），并尝试再次提交当前任务
* DiscardPolicy 丢弃当前任务

### submit与execute的区别

* submit可以catch异常
* submit可以响应数据
* 参数不一致

JVM
===

### OutOfMemoryError

* OutOfMemoryError： PermGen space 加载了大量的类和jar包，永久区满<br>
1.-XX:PermSize -XX:MaxPermSize 调整永久区大小<br>
2.删除多余重复的jar包<br>
* OutOfMemoryError：  Java heap space 对象实例太多，堆空间满<br>
1.检查程序，查看是否有优化空间<br>
2.调整Xmx和Xms大小<br>
* OutOfMemoryError：unable to create new native thread



## 命令工具

* jps 查看java进程
* jstat 查看虚拟机运行时信息
* jinfo 查看虚拟机参数
* jmap 导出堆文件
* jhat 堆分析工具
* jstack 查看线程堆栈
* jstatd 查看远程主机信息

### 标记清除法

先通过根节点标记所有可达对象，然后将没有标记的对象全部清除

缺点:清除后产生空间碎片

### 复制算法

将原有空间内存分为两块，每次只使用其中一块，在垃圾回收时，将正在使用的内存中的存货对象复制到未使用的内存中，之后清除正在使用的内存块的所有对象

新生代穿行垃圾回收器使用了复制算法的思想，新生代分为Eden、from和to三个空间，其中from和to空间可以视为用于复制的两块大小相同，地位相等且可进行角色互换的空间块

垃圾回收eden，from会进入to，有些对象会进入老生代

缺点:需要两块一样大小的空间，空间利用率低

### 标记压缩算法

在标记清除的算法上做优化，清除所有未标记对象后将剩余存活对象压缩到一块儿

适合老生代

### CMS回收器

* 初始标记:标记根对象(独占)
* 并发标记:标记所有对象
* 预处理:做清理准备以及控制停顿时间
* 重新标记:修正并发标记数据(独占)
* 并发清理:清理垃圾
* 并发重置:重置CMS数据，为下一次清理做准备

* -XX:+UseConcMarkSweepGC:使用CMS
* -XX:-CMSPrecleaningEnabled 关闭预清理
* -XX:ConcGCThreads -XX:ParallelCMSThreads 垃圾回收锁使用的线程数
* -XX:CMSInitiatingOccupancyFranction 回收阈值，默认68
* -XX:+UseCMSCompactAtFullCollection 开启垃圾回收后进行内存整理
* -XX:+CMSFullGCsBeforeCompaction 进行多少次垃圾回收后进行内存整理

### G1回收器

* 初始标记:标记从根节点可直达的对象，伴随着一次新生代GC(独占)
* 根区域扫描:扫描survivor区域直接可达的老年代区域，并标记这些可达对象
* 并发标记:扫描整个堆的存活对象，该过程可能被新生代GC打断
* 重新标记:修正并发标记数据（独占）
* 独占清理:标记需要回收的区域(独占)
* 并发清理阶段:清理空闲区域

数据库
===

### 聚集索引

* 叶子节点存的是整行数据，直接通过这个聚集索引的键值找到某行数据
* 数据的物理存储顺序与索引顺序是一致的（索引相邻则数据必然相邻）
* 一个表只能有一个聚集索引（primary key）

### 非聚集索引

* 叶子节点存的字段的值，通过这个非聚集索引的键值找到聚集索引字段的值，再通过聚集索引找到具体的行

### MyISAM与InnoDb的区别

* MyISAM是非事务安全的，而InnoDB是事务安全的
* MyISAM锁的粒度是表级锁，而InnoDB是行级锁
* MyISAM支持Fulltext全文类型索引，而InnoDB不支持
* MyISAM相对简单，效率上要优于InnoDB，小型数据库可以考虑使用MyISAM
* MyISAM表保存成文件，跨平台使用更方便

### 不会用到索引的情况

* 列与列对比，当一个表两个列分别都创建了索引，将他们进行对比，不会走索引
* where 条件与null判定不会走索引
* 否定条件！=、not、not exists不会走索引
* 前置通配符“%三” 不会用到索引
* where条件用到函数以及谓词运算（+-×/）
* where 条件类型不一致
* 组合索引最左原则
* or 条件只有两个列都有索引才会用到索引
* 连接查询关联关键词编码格式不一致
* 全表扫描快于使用索引（表数据量少）

### 怎么排除慢查询

* 通过配置日志参数可以捕获一些慢查询（slow_query_log=NO,slow_query_log_file, long_query_time,long_queries_not_using_indexes）
* 通过show processlist命令查看正在运行的语句（ID，user，host，db，command，time，state，info）
* explain了解语句执行的状态（table，possible_keys,key,key_len,ref,rows,Extra）

### 事务的四个特性

在可靠数据库管理系统中，事务具有的四个特性：原子性（Atomicity），一致性（Consistency），隔离性（Isolation），持久性（Durability）

* 原子性：一组指令，要么全部执行成功，要么全部不执行
* 一致性：事务执行使数据从一个状态转为另一个状态，但对于整个数据的完整性保持稳定
* 隔离性：多个用户访问数据库时，数据库为每一个用户开启事务，不被其他事务所干扰，多个并发事务之间相互隔离。
* 持久性：事务执行之后对于他的数据的改变是永久性的

### 事务的隔离级别

不同隔离级别可能引发的问题：

* 脏读:读取到其他事务尚未提交的的数据，可能被回滚
* 幻读(虚读):同一事务读取两次数据库，得到两个不同的接过（insert/delete满足条件的数据）
* 不可重复读:同一事务读取两次同一行数据得到两个不同的结果（被其他事务update）
* 更新丢失：两个事务修改同一行数据，后者覆盖了前者的修改

隔离级别：

* Read uncommitted：最低级别，可以读取未提交的数据，可能引发脏读
* Read committed：一个事务必须等另一个事务提交之后才能读取到相关数据，可避免脏读
* Repeatable read:重复读，在开始读取数据时，不再允许修改操作
* Serializable：最高级别，序列化，事务顺序化执行，效率低，可避免脏读、幻读、不可重复读

大多数据库的默认隔离级别为read committed，mysql为repeatable read，隔离级别只对当前链接有用

网络
===

### TCP三次握手

第一次握手：建立连接时，客户端发送SYN（syn=1，seq=x）包到服务器，并进入SYN_SENT状态，等到服务器确认<br>
第二次握手：服务器收到SYN包，必须确认客户的SYN（ack=x+1），同时自己也发送一个SYN包（seq=y，ack=x+1），即SYN+ACK包，此时服务器进入SYN_RECV<br>
第三次握手：客户端收到SYN+ACK包，向服务器发送确认包ACK（ack=y+1），此包发送完毕，客户端和服务器进入ESTABLISHED，完成三次握手

### TCP的四次挥手

* 客户端进程先向服务器发送（FIN=1，seq=x），并停止再发送数据，主动关闭TCP链接，进入FIN-WAIT-1状态
* 服务端受到释放报文段后立即发出确认报文（FIN=1，seq=y），服务器进入CLOSE_WAIT,此时TCP处于半关闭状态，客户端到服务器的连接释放
* 客户端收到服务器的确认后，进入FIN-WAIT-2,等待服务器发出链接释放状态
* 服务器发送数据完毕后，发出（FIN=1，ACK=1，seq=z，ack=x+1），服务器进入LASK-ACK等待A的确认
* 客户端收到服务端的确认后，发出（ACK=1，seq=x+1，ack=z+1），客户端进入TIME-WAIT状态，经过2MSL后，进入CLOSED状态

### 为什么三次握手而不是两次握手

主要是为了防止已失效的连接请求保温突然又传送到服务器而产生错误

### SYN攻击

服务端的资源分配是在二次握手时分配的，SYN攻击就是客户端短时间伪造大量不存在的IP地址，并向服务器不断发送SYN包，这些伪造的SYN包将长时间占用未链接的队列导致正常的SYN请求因为队列满而背丢弃，从而引起网络拥堵甚至系统瘫痪

防范措施：降低主机的等待时间使主机尽快释放半连接的占用，短时间受到同一IP的重复SYN则放弃后续请求

### 为什么TIME—WAIT必须等待2MSL的时间呢

* 确保ACK报文能够送达服务器
* 确保本次链接的报文在网络中消失，使下一次连接中不再出现旧的报文

### 关闭为什么需要四次握手

因为SYN请求只是用来同步的，服务端可以直接应答，但是收到FIN请求可能不能立即关闭SOCKET，所以先回复一个ACK报文，等所有报文都发送完毕之后再发送FIN报文

### 已建立链接，但是客户端出现故障

TCP设有一个保活计数器，服务器每收到一个客户端请求后就会重新复位这个计数器，通常时间为2小时，当超过2小时还没有收到任何数据，就会发送一个探测报文，每隔75s发送一次，发送10次报文仍没有反应，服务器就认为客户端出现故障，关闭连接

### TCP与UDP的区别

TCP：面向连接、可靠的字节流服务，客户端与服务器交换数据之前，必须先在双方建立一个TCP连接，之后才能传输数据，提供超时重发，丢弃重复数据，校验数据，控制流量等功能

UDP：是一个简单的面向数据的运输层协议，不可靠，只是应用程序传给IP层的数据报文发送出去，但是不能保证他们能到达目的，特点传输速度快，最大长度64k，分包无法保证包序

## select

各个客户端连接的套接字，都被放到一个集合中，调用select之后会一直监视这些文件描述符有哪些可读（遍历），如果有可读的描述符，那么我们的工作进程就去读取资源

## poll

实现与select类似，但是select只能维持1024个连接，poll在这个基础上做了加强，可以维持任意数量的连接

## epoll

套接字数量无限制，基于内核的反射机制，在有活跃的sockt时，系统会调用提前设置的回调函数<br>
当大多数客户端都很活跃时，会导致所有回调函数都背唤醒，导致负载较高，范围select/poll更好

### Http与Https的区别

* 工作层：在OSI网络模型中，HTTP工作于应用层，而HTTPS工作在传输层。
* 连接端口：HTTP标准端口是80，而HTTPS的标准端口是443。
* 传输方式：HTTP是超文本传输协议，信息是明文传输，而HTTPS是SSL加密传输协议。
* 工作耗时：HTTP耗时=TCP握手，而HTTPS耗时=TCP握手+SSL握手。
* 显示形式：HTTP的URL以http://开头，而HTTPS的URL以https://开头。
* 费用：HTTP无需费用，而HTTPS需要到CA申请证书，一般免费证书较少，需要一定费用。
* 安全性：HTTP的连接很简单，是无状态的；HTTPS协议是由SSL+HTTP协议构建的可进行加密传输、身份认证的网络协议，比HTTP协议安全。

### Http状态码

* 1**-服务器收到请求，需要请求者继续执行操作
* 2**-成功接收并处理
* 3**-重定向，需要进一步的操作完成处理
* 4**-客户端错误
* 5**-服务端错误

* 500-Internal Server Error 服务器内部错误，无法完成任务
* 501-NotImplemented 服务器不支持请求的功能，无法完成请求
* 502-Bad Gateway 代理网关服务器收到一个无效的请求
* 503-Service Unavailable 由于超载或者系统维护，服务器暂时无法响应客服端的请求
* 504-Gateway Time-out 代理网关服务器未能及时从远端服务器获取请求
* 505-Http Version not supported 服务器不支持请求的协议版本

### Session和Cookie

Cookie以文本形式存储在浏览器上，一般不超过4Kb，不安全,Session以K-V形式存储在服务端

* Cookie以文本形式存储在浏览器上/8520且大小一般不超过4kb，Session存储在服务端,内存一般不限制
* 可以轻松访问Cookie，但是不能轻易访问Session，所以Session更安全

消息队列
===

消息队列的作用：解耦，异步，错峰

rabbitMQ的替代方式



缓存
===

### Redis主从同步

全量同步:一般发生在Slave初始化阶段，这时候需要将Master上的所有数据复制一份

* 从服务器链接主服务器，发送SYNC命令
* 主服务器收到SYNC命令后，开始执行BGSAVE命令生成RDB文件并使用缓存区记录此后执行的所有命令
* 主服务器执行完BGSAVE之后向所有从服务器发送快照文件，并继续记录执行的命令
* 从服务器收到快照文件后丢弃所有旧数据，载入收到的快照
* 主服务器发送完文件后开始发送缓存区中的指令
* 从服务器载入快照完成后执行接收到的缓存区指令

增量同步:Slave初始化完成之后正常工作从主服务器同步到从服务器的过程

* 主服务器没执行一条命令就将命令发送到从服务器

### Redis持久化

RDB：定时将redis中数据dump到硬盘中<br>
AOF:根据操作日志文件记录数据

RDB优点:文件小，恢复快，易恢复<br>
RDB缺点:最后一次备份之后的数据会丢失，备份时占用CPU过多

AOF优点:数据不易丢失<br>
AOF缺点:备份文件大


设计
===

## 设计模式

### 简单工厂

通过静态方法的不同参数创建不同类实例

优点：<br>
* 包含了必要的判断逻辑，实现了类的创建和使用的分离
* 不需要关注具体产品的类名，只需要关注产品类具体的参数
* 容易添加新的产品类，系统灵活性较高

缺点：<br>
* 工厂类职责过重，出现问题影响面积大
* 新加产品类需要修改工厂方法，违反了开放-封闭原则
* 静态方法无法形成继承的等级结构

### 方法工厂

每一个工厂类生成对应的产品类

优点:<br>
* 隐藏了产品类实例化的细节
* 新增产品类直接增加工厂类即可，符合开放-闭合原则
* 工厂都继承了自己的父类，体现了多态性

缺点:<br>
* 新增产品类必须同时新增工厂类
* 抽象层的加入影响理解

### 抽象工厂

在工厂方法上面进行衍生，提供更强大的工厂类和可拓展性，同一接口可以生成多个不同的产品类

优点:<br>
* 新增一个一个工厂类即可生成相对应的所有产品，符合开放-封闭原则

缺点:<br>
* 新增产品类，所有继承该接口的工厂类都要增加对应的工厂方法，违反了开放-封闭原则

## 简单工厂、方法工厂、抽象工厂的区别

三种模式各有利弊，简单工厂违反了最基本的开放-封闭原则，工厂方法存在的工厂类过多，导致系统庞大，抽象方法新增产品族很方便，但是新增产品类很麻烦