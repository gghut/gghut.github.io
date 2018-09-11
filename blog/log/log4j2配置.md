log4j2配置
====

springboot 配置log4j2
-----

http://blog.didispace.com/springbootlog4j/

# 依赖

springboot 1.3.x及其以下版本支持log4j，1.4.x及其以上版本只支持log4j2和logback

```xml
    <dependency>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter</artifactId>
        <exclusions>
            <exclusion>
                <groupId>org.springframework.boot</groupId>
                <artifactId>spring-boot-starter-logging</artifactId>
            </exclusion>
        </exclusions>
     </dependency>
       
     <dependency> 
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-log4j2</artifactId>
     </dependency>
```

```properties
log4j.rootLogger=info,ServerDailyRollingFile,stdout

log4j.appender.ServerDailyRollingFile=org.apache.log4j.DailyRollingFileAppender
log4j.appender.ServerDailyRollingFile.DatePattern='.'yyyy-MM-dd
log4j.appender.ServerDailyRollingFile.File=D://test/test.log
log4j.appender.ServerDailyRollingFile.layout=org.apache.log4j.PatternLayout
log4j.appender.ServerDailyRollingFile.layout.ConversionPattern=%d{yyyy-MM-dd HH:mm:ss} [%t] %-5p [%c] - %m%n
log4j.appender.ServerDailyRollingFile.Append=true

log4j.appender.stdout=org.apache.log4j.ConsoleAppender
log4j.appender.stdout.layout=org.apache.log4j.PatternLayout
log4j.appender.stdout.layout.ConversionPattern=%d yyyy-MM-dd HH:mm:ss %p [%c] %m%n
```