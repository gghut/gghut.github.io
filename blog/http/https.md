HTTPS
===

TCP与UDP
---

TCP：面向连接、可靠的字节流服务，客户端与服务器交换数据之前，必须先在双方建立一个TCP连接，之后才能传输数据，提供超时重发，丢弃重复数据，校验数据，控制流量等功能

UDP：是一个简单的面向数据的运输层协议，不可靠，只是应用程序传给IP层的数据报文发送出去，但是不能保证他们能到达目的，特点传输速度快，最大长度64k，分包无法保证包序


http为什么不安全
---

http协议因为没有任何的加密以及身份验证机制，非常容易遭到窃听、劫持、篡改等

TCP三次握手
---

第一次握手：建立连接时，客户端发送SYN（syn=1，seq=x）包到服务器，并进入SYN_SENT状态，等到服务器确认<br>
第二次握手：服务器收到SYN包，必须确认客户的SYN（ack=x+1），同事自己也发送一个SYN包（seq=y，ack=x+1），即SYN+ACK包，此时服务器进入SYN_RECV<br>
第三次握手：客户端收到SYN+ACK包，向服务器发送确认包ACK（ack=y+1），此包发送完毕，客户端和服务器进入ESTABLISHED，完成三次握手

### 为什么三次握手而不是两次握手

主要是为了防止已失效的连接请求保温突然又传送到服务器而产生错误

### SYN攻击

服务端的资源分配是在二次握手时分配的，SYN攻击就是客户端短时间伪造大量不存在的IP地址，并向服务器不断发送SYN包，这些伪造的SYN包将长时间占用未链接的队列导致正常的SYN请求因为队列满而背丢弃，从而引起网络拥堵甚至系统瘫痪

防范措施：降低主机的等待时间使主机尽快释放半连接的占用，短时间受到同一IP的重复SYN则放弃后续请求

四次挥手
---

客户端进程

* 客户端进程先向服务器发送（FIN=1，seq=x），并停止再发送数据，主动关闭TCP链接，进入FIN-WAIT-1状态
* 服务端受到释放报文段后立即发出确认报文（FIN=1，seq=y），服务器进入CLOSE_WAIT,此时TCP处于半关闭状态，客户端到服务器的连接释放
* 客户端收到服务器的确认后，进入FIN-WAIT-2,等待服务器发出链接释放状态
* 服务器发送数据完毕后，发出（FIN=1，ACK=1，seq=z，ack=x+1），服务器进入LASK-ACK等待A的确认
* 客户端收到服务端的确认后，发出（ACK=1，seq=x+1，ack=z+1），客户端进入TIME-WAIT状态，经过2MSL后，进入CLOSED状态

### 为什么TIME—WAIT必须等待2MSL的时间呢

* 确保ACK报文能够送达服务器
* 确保本次链接的报文在网络中消失，使下一次连接中不再出现旧的报文

### 关闭为什么需要四次握手

因为SYN请求只是用来同步的，服务端可以直接应答，但是收到FIN请求可能不能立即关闭SOCKET，所以先回复一个ACK报文，等所有报文都发送完毕之后再发送FIN报文

### 已建立链接，但是客户端出现故障

TCP设有一个保活计数器，服务器每收到一个客户端请求后就会重新复位这个计数器，通常时间为2消失，当超过2小时还没有收到任何数据，就会发送一个探测报文，每隔75s发送一次，发送10次报文仍没有反应，服务器就认为客户端出现故障，关闭连接

IO复用
---

## select

各个客户端连接的套接字，都被放到一个集合中，盗用select之后会一直监视这些文件描述符有哪些可读（遍历），如果有可读的描述符，那么我们的工作进程就去读取资源

## poll

实现与select类似，但是select只能维持1024个连接，poll在这个基础上做了加强，可以维持任意数量的连接

## epoll

套接字数量无限制，基于内核的反射机制，在有活跃的sockt时，系统会调用提前设置的回调函数<br>
当大多数客户端都很活跃时，会导致所有回调函数都背唤醒，导致负载较高，范围select/poll更好