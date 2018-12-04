springboot 邮件发送
====

依赖
---

```xml
<dependency>
	<groupId>org.springframework.boot</groupId>
	<artifactId>spring-boot-starter-mail</artifactId>
</dependency>
```

```yml
spring:
  mail:
    host: smtp.126.com
    username: 邮箱账号
    password: 邮箱授权码
```

```java
@Component
public class MailHandler {

    private JavaMailSender jms;

    public MailHandler(JavaMailSender jms) {
        this.jms = jms;
    }

    public void send(){
        //建立邮件消息
        SimpleMailMessage mainMessage = new SimpleMailMessage();
        //发送者
        mainMessage.setFrom("邮箱账号");
        //接收者
        mainMessage.setTo("收件人");
        //发送的标题
        mainMessage.setSubject("邮件标题");
        //发送的内容
        mainMessage.setText("邮件内容");
        jms.send(mainMessage);
    }
}
```