函数式编程
===

* 函数可以作为参数，可以作为响应值

## FunctionalInterface

* 表明接口是一个函数式接口，注解不需要显式标注
* 只能有一个抽象方法，被Object实现的方法不是抽象方法

### 接口默认方法

* 能包含若干实例方法
* 使用关键字default定义
* 接口默认方法冲突要在实现类中重写指定Interface.super.method();

## lambad表达式

匿名函数，可以作为参数传给调用者

* 访问外部对象，对象需要用final修饰

### 方法引用

* 静态方法ClassName::methodName
* 实例的实例方法instanceReference::methodName
* 超类方法super::methodName
* 类型上的实例方法ClassName::methodName
* 构造方法Class::new
* 数组的构造方法TypeName[]::new

如果使用静态方法或者目标明确，流内元素会自动作为参数使用。如果函数引用表示实例方法，并且不存在调用目标，那么流内元素就会作为调用目标

## parallel并行

* parallel()
* parallelStream()
.parallelSort()

## CompletableFuture 

后续补充
