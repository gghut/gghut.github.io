高并发
====

基本概念
----

同步：同步方法调用一旦开始，调用者必须等到调用调用返回后，才能继续后续行为<br>
异步：异步方法调用一旦开始，方法调用就会立即返回，调用者可以继续后续操作

并发：多任务交替执行，而多个任务之间有可能还是串行<br>
并行：多任务同时进行（在不同资源上）

临界区：表示一种公共资源或者说共享数据，可以被多个线程使用，但每一次只能有一个线程使用他，一旦临界区资源被占用，其他线程要使用这个资源必须等待

多线程间的相互影响<br>
* 阻塞,当一个线程占用了临界区资源，其他所需要这个资源的线程就必须进行等待（挂起）<br>
* 非阻塞,没有一个线程可以妨碍其他线程执行

多线程的活跃性问题<br>
* 死锁,彼此之间占用了其他线程所需的资源且得不到释放<br>
* 饥饿,因为各种原因得不到所需要的资源，例如线程优先级低等<br>
* 活锁,相互之间谦让资源却到恰好占据多方所需资源

并发级别<br>
* 阻塞，其他线程在释放资源之前，当前线程无法继续执行
* 无饥饿，使用公平锁，每个线程都有获得资源的机会；反之非公平锁，可能造成饥饿
* 无障碍，线程不会因为临界区资源导致另一方被挂起，当检测到数据被错误修改会进行回滚
* 无锁，所有线程都能尝试对临界区进行访问，保证必然有一个线程能够在有限步内完成操作离开临界区
* 无等待，所有线程都必须在有限步内完成操作离开临界区

java内存模型（JMM）<br>
保证并发程序中的数据访问的一致性和安全性<br>
原子性：一个操作是不可中断的<br>
可见性：当一个线程修改了某一共享变量，其他线程能够立即知晓这个修改<br>
有序性：指令重排，一段没有严格前后执行要求的代码可能排列顺序会颠倒，对当前线程执行不会产生影响，但对其他线程可能产生影响

* volatile可以提升变量的原子性、可见性、有序性(仅限于声明、定义、修改，i++类操作不具备原子性)

### 线程的状态

```java
public enum State{
    NEW,//新建，还未执行
    RUNNABLE,//开始执行，调用start()之后
    BLOCKED,//遇到synchronized
    WAITING,//调用wait()
    TIMED_WAITING,//调用wait(long timeoutMillis)
    TERMINATED;//执行结束
}
```

### 线程的停止与中断

中断的效果强于停止（通过标志位停止线程而非stop()），当线程进入sleep()或者wait()时，必须要中断才能识别，且中断后抛出InterruptedException并重置中断标志位，若需在代码中再次验证中断标志需在catch部分再次设置设置中断

### wait()与notify()

wait()和notify()必须包含在synchronized语句中，在执行wait()前必须获得object的监视器，wait()执行后会释放这个监视器（防止其他等待在object对象上的线程因为该线程休眠而全部无法正常执行），执行notify会唤醒对象等待队列的随机一个线程，且在唤醒前需先获得监视器，当线程背唤醒后也会先重新获得对象的监视器，才能执行后续代码

### wait()和sleep()

* wait()方法可以被唤醒
* wait()会释放目标对象锁，而sleep()不会释放任何资源

### join()和yeild()

join()的实现实际上是while(isAlive()){wait(0)}，且wait的对象为当前线程对象，所以切勿在Thread对象上使用wait()或者notify()方法，否者会影响系统API

### 线程组

```java
ThreadGroup tg = new ThreadGroup("thread-group-name");
Thread thread = new Thread(tg, new ImplementsRunnable(), "thread");
thread.start();
tg.activeCount();//输出活动线程总数，为估算值，无法精确
tg.list();//打印线程组中所有的线程信息
```

### 守护线程(Daemon)

* 当用户线程全部结束，仅剩守护线程时，JAVA虚拟机就会自然退出
* 守护线程必须在start()之前设置

### 线程优先级

* 1到10，数字越大，优先级越高

### 重入锁

```java
ReentrantLock lock = new ReentrantLock();
int i = 0;
lock.lock();
try{
    i++;
}finally{
    lock.unlock();
}
```

* 可以多次使用，一次lock()对应一次unlock()
* lock.lockInterruptibly()可以对中断进行响应，在等待锁的过程中，可以响应中断(synchornized不能，但是wait()能)
* lock.lock()获得锁，如果锁已经背占用，则等待
* lock.tryLock(3, TimeUnit.SECONDS)限时等待,获得锁返回true，没有获得返回false，无参数立即返回
* 默认为非公平锁，new ReentrantLock(true)为公平锁

```java
ReentrantLock lock = new ReentrantLock();
Condition condition = lock.newCondition();
try {
    condition.await();
} catch (InterruptedException e) {
    e.printStackTrace();
}
condition.awaitUninterruptibly();
condition.signal();
```

* wait()与object.wait()类似，当前线程进入等待，释放当前锁，当其他线程是signal()或者signalAll()时，线程会重新获得锁并继续执行，线程被中断也能跳出等待
* awaitUninterruptibly()与wait()类似，但是不会响应中断
* signal()与notify()方法类似

### 信号量

最大同时可访问的线程数

```java
public Semaphore(int permits);
public Semaphore(int permits, boolean fair);
```

* acquire()尝试获得准入许可，无法获得进入等待
* acquireUnInterruptibly()不响应中断
* tryAcquire()尝试获得，成功true，失败false，不进行等待
* release()释放一个许可

### 读写锁 ReentrantReadWriteLock

* 适用于多读少写
* 读读不互斥，读写、写写互斥

### 倒计数器 CountDownLatch

```java
CountDownLatch cdl = new CountDownLatch(10);
cdl.countDown();
cdl.await();
```

* 初始化设置计数个数
* countDown()每次执行减一
* await()进入等待，计数归零后继续执行

### 循环栅栏 CyclicBarrier

```java
public CyclicBarrier(int parties, Runnable barrierAction);
cyclicBarrier.await();
```

* parties参与循环的线程任务数量
* barierAction一次全体await()之后执行的任务
* await()执行次数等于parties之后执行barrierAction
* 当有任务不能正常完成（例如出现InterruptedException）之后，其他线程报BrokenBarrierException，代表任务已经无法完成了

### LockSupport

* 线程阻塞工具，可以在任意未知让线程阻塞
* unpark()方法可以放生在park()之前，他可以是park()方法立即返回
* 中断不会抛出InterruptedException且可以直接从Thread.interrupted()方法中获得中断标记

### RateLimiter

漏桶算法：以固定流速通过请求<br>
令牌算法：单位时间内生成令牌，一个请求消耗一个令牌

```java
RateLimiter limiter = Ratelimiter.create(2);
limiter.acquire();
limiter.tryAcquire();
```

* RateLimiter采用令牌桶算法
* tryAcquire()不阻塞，成功返回ture，失败返回false

## 线程池

为了避免系统频繁的创建和销毁线程，让创建的线程复用

```java
public ThreadPoolExecutor(int corePoolSize,
                            int maximumPoolSize,
                            long keepAliveTime,
                            TimeUnit unit,
                            BlockingQueue<Runnable> workQueue)
public ThreadPoolExecutor(int corePoolSize,
                            int maximumPoolSize,
                            long keepAliveTime,
                            TimeUnit unit,
                            BlockingQueue<Runnable> workQueue,
                            ThreadFactory threadFactory,
                            RejectedExecutionHandler handler)

```

* corePoolSize 指定线程池中的线程数量
* maxinumPoolSize 指定线程池中的最大线程数量
* keepAliveTime 当线程池中线程数量操作corePoolSize时，多余的空闲线程的存活时间
* unit keepAliveTime的单位
* workQueue 任务队列，被提交但尚未被执行的任务
* threadFactory 线程工厂，用于创建线程，一般使用默认
* handler 拒绝策略，当超过workQueue最大容量时采用拒绝策略

```java
public static ExecutorService newFixedThreadPool(int nThreads) {
    return new ThreadPoolExecutor(nThreads, nThreads,
                                    0L, TimeUnit.MILLISECONDS,
                                    new LinkedBlockingQueue<Runnable>());
}
```

```java
public static ExecutorService newSingleThreadExecutor() {
    return new FinalizableDelegatedExecutorService
        (new ThreadPoolExecutor(1, 1,
                                0L, TimeUnit.MILLISECONDS,
                                new LinkedBlockingQueue<Runnable>()));
}
```

```java
public static ExecutorService newCachedThreadPool() {
    return new ThreadPoolExecutor(0, Integer.MAX_VALUE,
                                    60L, TimeUnit.SECONDS,
                                    new SynchronousQueue<Runnable>());
}
```

* 直接提交的队列，SychronousQueue对象提供，是一个特殊的BlockingQueue，没有容量，每一个插入操作就要等待相应的删除操作，反之，每一个删除操作都要等待对应的插入操作，总是将任务提交给线程执行，没有空闲线程执行拒绝策略
* 有界任务队列，ArrayBlockingQueue，线程池实际线程数少于corePoolSize，则创建新线程，大于corePoolSize，则加入等待队列，若等待队列已满，且线程数量小于maxinumPoolSize，创建新线程，若大于maxinumPoolSize，则执行拒绝策略
* 无界任务队列，LinkedBlockingQueue，不会用到大于corePoolSize到maxinumPoolSize这个阶段数量的线程，除非内存耗尽，否则大于corePoolSize的任务都会加到任务队列

### 拒绝策略

* AbortPolicy 直接抛出异常，阻止系统正常工作
* CallerRunsPolicy 由调用者执行当前任务
* DiscardOldestPolicy 丢弃任务队列中最老的一个请求（即将执行的），并尝试再次提交当前任务
* DiscardPolicy 丢弃当前任务

### 合理的线程池数量

* Ncpu cpu的数量（Runtime.getRuntime().availableProcessiors()）
* Ucpu 目标cpu的使用率
* W/C 等待（wait）时间与计算（calculate）时间的比率

```java
    Nthreads = Ncpu * Ucpu * (1 + W/C)
```

### submit()和execute()的区别

```java
Future<?> submit(Runnable task);
<T> Future<T> submit(Callable<T> task);
<T> Future<T> submit(Runnable task, T result);

void execute(Runnable command);
```

* 接收的参数不一样
* submit有返回值，而execute没有
* submit方便Exception处理

### ForkJoinPool

```java
ForkJoinPool forkJoinPool = new ForkJoinPool();
public <T> ForkJoinTask<T> pool.submit(ForkJoinTask<T> t);
```

* ForkJoinTask有两个重要的子类RecursiveAction和RecursiveTask，他们支持fork()方法分解及join()方法等待任务
* RecursiveTask有返回值，get()计算结束之前等待，结束之后返回，RecursiveAction没有返回值
* 当一个线程试图帮助其他线程时，总是从任务队列的底部获取数据，而线程执行自己任务时总是从顶部开始获取数据
* 默认线程数Runtime.getRuntime().availableProcessors()

### DirectExecutor

```java
Executor executor = MoreExecutor.directExecutor();
```

* 并没有真正的创建或者使用额外线程，总是将任务在当前线程执行

### Daemon 线程池

```java
MoreExecutors.getExitingExecutorService(executor)
```

* 将executor中的线程设置为守护线程

## 提高锁性能

* 减少锁持有的时间-将不需要占用临界区资源的代码（前后）放置在锁外
* 减小锁的粒度，分成多个锁
* 读写锁替换独占锁，读读不互斥
* 锁分离，只锁需要访问部分的临界区资源，不需要访问的部分的数据提供给其他线程访问
* 锁粗化，同步、释放会消耗较多资源，所以连续多个锁合并为一个

### java虚拟机对锁的优化

* 锁偏向，同一线程再次请求锁可节省大量有关锁的申请操作，反之竞争激烈的场景效果欠佳，-XX:+UseBiasedLocking开启偏向锁
* 轻量级锁，偏向锁失败不会立即挂起线程，而是使用轻量级锁，他将对象头部作为指针指向持有锁的线程内部，如果获得轻量级锁则可以进入临界区，如果其他线程抢到锁，那么当前线程的锁请求就会膨胀撑重量级锁
* 自旋锁，锁膨胀后虚拟机最后的尝试，让当前线程做几个空循环，避免线程刚被挂起就获得锁
* 锁消除，消除不可能竞争资源的锁，节省无意义的请求锁时间

## ThreadLocal

线程局部变量，只有当前线程可以访问

```java
ThreadLocal<T> tl = new ThreadLocal<>();
t1.set(new T());
t1.get()
```

原理需补充

## 乐观锁与悲观锁

* 悲观锁，认为每一次的临界区操作都会产生冲突
* 乐观锁，认为每一次的临界区操作都是没有冲突的

无锁，比较交换（CAS），一旦检测到冲突就进行重试，直到没有冲突为止，开销小，性能更优越<br>
CAS(V,E,N)，V表示要更新的变量，E表示预期值，N表示新值，当V值等于E值时，才会将V值设置为N，如果V、E不同，则说明其他线程做了更新，原子操作

### AtomicInteger

线程安全的的整数包装类，内部CAS操作

* private volatile int value 代表当前实际值
* static final long valueOffset value在对象中的偏移量

### Unsafe

不安全的指针操作，内部采用CAS操作

### AtomicRefference

线程安全的对象

### AtomicStampedReference

内部包含时间戳，必须对象值和时间戳都满足预期才能写入成功

### AtomicIntegerArray，AtomicLongArray，AtomicReferenceArray

CAS的数组操作

### AtomicIntegerFieldUpdater，AtomicLongFieldUpdater，AtomicReferenceFieldUpdater

让普通对象可以进行CAS修改，实现原理为反射，变量必须为volatile修饰，不支持静态变量

# 并行模式

* 单例模式，仅有一个实例
* 不变模式，对象被创建后内容不能被修改，去除setter方法，属性设置为private final,不能被重载，通过构造方法设置属性值
* 生产消费者模式，生产者，消费者，内容缓存区（BlockingQueue性能较低），任务
* 无锁的生产者消费者，缓冲区使用ConcurrentLinkedQueue(CAS操作困难),Disruptor框架使用无锁的方式实现了环形队列（RingBuffer）
* Future模式，有限完成其他任务，到真正需要数据的时候再去尝试获得需要的数据

## 并行搜索

分段搜索

## 并行排序

* 奇偶排序 指定奇数位与后一位进行比较交换，再指定偶数位与后一位进行比较交换
* 希尔排序 每隔h个单位抽取一个子数组，总共h个子数组，进行间隔为h的插入排序，再依次将h递减

## NIO

## AIO

http再细了解


