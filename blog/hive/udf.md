UDF
===

udf
---

* org.apache.hadoop.hive.ql.exec.UDF
* 支持基础数据类型(Text,IntWritable,LongWriable,DoubleWriable)
* 调用evaluate方法

```java
import org.apache.hadoop.hive.ql.exec.UDF;

public class ClassName extends UDF{
    public String evaluate(){
        return "hello world!";
    }

    public String evaluate(String str){
        return "hello world: " + str;
    }
}
```

```sh
javac -classpath $HIVE_HOME/lib/hive-exec-<hive version>.jar <package>/TestHello.java
jar -cvf <jar_name>.jar <package>/TestHello.class
```

```sql
add jar <jar_name>.jar
create temporary function <function_name> as '<package>.<class_name>'
```

GenericUDF
---

* org.apache.hadoop.hive.ql.udf.generic.GenericUDF

```java
// 这个类似于简单API的evaluat方法，它可以读取输入数据和返回结果  
abstract Object evaluate(GenericUDF.DeferredObject[] arguments);

// 该方法无关紧要，我们可以返回任何东西，但应当是描述该方法的字符串  
abstract String getDisplayString(String[] children);

// 只调用一次，在任何evaluate()调用之前，你可以接收到一个可以表示函数输入参数类型的object inspectors数组  
// 这是你用来验证该函数是否接收正确的参数类型和参数个数的地方  
abstract ObjectInspector initialize(ObjectInspector[] arguments);
```