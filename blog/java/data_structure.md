Java的数据结构
===

基本数据结构
----

## 数组

```java
int[] array = new int[10];
int[] array = new int[]{1,2};

String[] array = new String[2];
String[] array = new String[]{"a","b"};
```

## 链表

```java
public class Node<T>{
    private Node next;
    private T value;
}
```

## 栈

```java
Stack stack=new Stack();
```

## 队列

```java
Queue<String> queue = new LinkedList<String>();
```

## 树

```java
public class Node<T>{
    private Node left;
    private Node right;
    private T value;
}
```

### 红黑树



## 堆

常用数据结构
===

# Collection

* 继承Iterable接口（iterator()、forEach()）
* 不需要设置初始值大小
* 不限制对象类型

# Set

* 不允许重复（equals判定）
* 变量类型分为基本类型用引用类型，基本类型可以直接通过==比较值,Date，Integer，Long等重写了equals，可以比较值
* equals和==都比较内存地址

## HashSet

* 最多只允许有一个null元素
* 元素顺序无法保证
* 用HashMap实现（key为hashSet的值，value为一个静态常量对象）

## TreeSet

详情见TreeMap

```java
public TreeSet() {
    this(new TreeMap<>());
}
```

## LinkedHashSet

LinkedHashMap实现

## CopyOnWriteArraySet

由CopyOnWriteArrayList实现，add由addIfAbsent()实现

# List

### ArrayList

* 使用数组实现，是一个动态数组，起容量能自动增长
* 无参构造方法创建的ArrayList容量为0，执行add操作首次判断后赋值为10，后续每次扩容为原来的1.5倍
* 多线程下可能会因为多线程在同一位置赋值导致数据被覆盖
* 多线程考虑Collections.synchronizedList(List i)
* 容量自动增长，重新像新数组拷贝数据，list.ensureCapacity(100)可以操作容量大小
* 不适合插入和删除，会大量移动数据

### CopyOnWriteArrayList

* 写时使用重入锁ReentrantLock
* 读的时候不需要锁
* 实现的载体任然为数组
* 读写分离，写时赋值出一个新的数组，完成插入、修改、删除等操作之后将新数组赋值给原array
* 适用于读多写少的场景
* 缺点，内存占用问题，每写一次就会新建一个数组对象，会频繁GC，数据一致性问题，只能保证最终一致性，不能保证实时一致性
* Vector使用Synchronized，性能略差与CopyOnWriteArrayList（读无锁）

### LinkedList

* 使用链表（双向链表）实现
* 实现Deque,可以作为双向链表使用
* 实现list，可以作为队列使用 
* 非同步的，线程不安全
* 两个重要的属性，first(头部节点)，last（尾部节点）,size（链表长度）
* 不善于查找，更适合增删改操作


### Vector

实战JAVA高并发196页
* 实现原理与ArrayList类似，都用数组实现，动态扩容
* 使用synchronized关键字保证线程安全
* 扩容大小算法不同，扩容因子为0则每次扩大为原来的两倍（加上原大小），不为零则每次在原来的基础上加上扩容因子

### Stack

继承至Vector,后进先出

* push 将元素压入栈顶（数组末尾，0为栈底，len-1为栈顶） 
* pop 弹出栈顶元素（peek之后再删除元素）
* peek 返回栈顶元素(返回数组最后一个元素)
* search 返回最靠近顶端的元素到栈顶的距离（lastIndexOf）


# queue

继承至Collection，先进先出

* offer() 将元素添加到队列尾部，成功返回true，否则false
* poll() 从队首删除并返回元素
* peek() 从队首返回元素但不删除

### ArrayQueue

## Deque

双向链表，实现类有LinkedList，ArrayDeque,ConcurrentLinkedDeque，LinkedBlockingDeque

* push() 将元素从队首加入队列，

### ArrayDeque

* 数组实现




## BlockingQueue

阻塞队列接口，实现类有ArrayBlockingQueue,LinkedBlockingQueue，PriorityBlockingQueue，DelayQueue,SynchronousQueue

使用重入锁ReentrantLock

### DelayQueue

 一个实现PriorityBlockingQueue实现延迟获取的无界队列，在创建元素时，可以指定多久才能从队列中获取当前元素。只有延时期满后才能从队列中获取元素

### ConcurrentLinkedQueue

### SynchronousQueue

实战JAVA高并发程序201页

## 非阻塞队列

实现类有PriorityQueue,ConcurrentLinkedQueue

# Iterator

# Map

## HashMap

### HashCode

* Object的HashCode返回对象内存地址经过处理后的结果
* String根据字符串内容经过特殊处理返回哈希码
* Integer直接返回数值本身

```java
Map<String, Object> map = new HashMap<>();
```

* 初始容量大小为16个元素
* key为null至多只能有一条

```java
static final int hash(Object key) {
    int h;
    return (key == null) ? 0 : (h = key.hashCode()) ^ (h >>> 16);
}
```

* map的hash是通过key的hashCode的高16位与低16位异或获得的

需要补充底层原理

### ConcurrentHashMap

322

两次hash，第一次hash确定segment，第二次确定数组的位置

## TreeMap

实现了SortedMap接口，他是有序的接口，红黑树接口，每个key-value都作为一个红黑树节点

key必须实现Comparable接口

## HashTable

继承与Dictionary，实现了Map，Cloneable，Serializable接口

方法是同步的，他是线程安全的，kv不能为null，key无序

补充原理及hashmap的区别

### HashMap与HashMap的区别

* 父类不同，hashMap继承自AbstractMap，hashTable继承自Dictionary
* HashMap线程不安全，HashTable使用Synchronized，线程安全
* HashMap只包含containsKey以及containsValue，HashTable包含contains（同containsKey）、containsKey，containsValue
* HashMap允许可以一个key为null，多个value为null，HashTable的key-value一个都不允许为null
* HashTable保留了Enumeration遍历方式
* HashTalbe直接使用hashCode取摸，HashMap运用hashCode的高16位与低16位做异或运算再取摸
* HashTable在不指定容量的默认值为11，扩容为old×2+1，HashMap为16，扩容为2×old

###ConcurrentSkipListMap

# Comparable



