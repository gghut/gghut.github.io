/usr/lib/jvm

tar zxvf jdk-8u121-linux-x64.tar.gz

sudo gedit /etc/profile

```java

export JAVA_HOME=/usr/lib/jvm/jdk1.8.0_121

export CLASSPATH=.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib:$CLASSPATH

export PATH=$JAVA_HOME/bin:$JAVA_HOME/jre/bin:$PATH

```

source /etc/profile

java -version