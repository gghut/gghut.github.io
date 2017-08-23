AUTH
====

2.0.0-SNAPSHOT
----

# 配置方法

新版本auth依然采用同1.*版本一致的通过在filter层拦截,检测请求的方式达到对用户请求进行认证授权的作用

## 抽象父类 AuthConfigurerAdapter

AuthConfigurerAdapter是整个Auth的入口,同时也是Auth的配置的主类

### Filter设置

AuthConfigurerAdapter实现了Filter接口,所以要使该类生效可以通过给其子类添加@WebFilter注解,或者将其子类通过FilterRegistrationBean注入到spring容器中,或者通过Filter标签添加到项目配置中

```java
@WebFilter(urlPatterns = {"/*"})
```

filter所配置的路径将受到auth的限制

### UserService配置

AuthConfigurerAdapter存在一个必须实现的抽象方法customUserService():UserService,该方法主要用于配置授权所用到的用户数据源

UserService是一个需要实现的接口,该接口中仅有一个loadUserByUsername(String:username):UserDetails的方法,该方法会在用户执行登录操作时调用

```java
public class UserDetails {
    private int uid;
    private String username;
    private String password;
    private Set<String> authorities;
}
```

从UserDetails类中可以看到,在loadUserByUsername方法中需要提供的有用户id,用户账号,用户密码,用户权限等,所以对应的这几项在数据库设计时是必须的项

### configure配置

```java
    @Override
    protected void configure(AuthConfig config){
    }
```

这是AuthConfigurerAdapter中的一个方法,主要用于重写对auth进行配置,其中的参数AuthConfig包含了auth的所有可配置项

```java
public class AuthConfig {
    private String loginPage = "/login.html";//默认登录页,修改将使用新的登录页
    private String loginDo = "/login.do";//默认登录地址,修改只会改变请求路径,请求由auth执行响应
    private String usernameParameter = "merchant_name";//默认用户名字段
    private String passwordParameter = "merchant_pwd";//默认密码字段
    private String logoutUrl = "/logout";//默认注销登录地址,修改只会改变请求路径,请求由auth执行响应
    private Map<Pattern, String> authorities = new HashMap();
    private UserService userService;
    private AuthenticationProvider authenticationProvider;
    private AuthenticationManager authenticationManager;
}
```

配置如下(仅有需要重写的部分才在配置中写出,使用默认配置的不需要写出)

```java
        config.formLoginBuilder()
                    .loginPage("/login")
                    .loginDo("/login.do")
                    .usernameParameter("username")
                    .passwordParameter("password")
                    .and()
                .logoutBuilder()
                    .logoutUrl("/logout")
                    .and()
                .authoritiesBuilder()
                    .authorities("/admin/*", "ROLE_ADMIN")
                    .authorities("/user/*", "ROLE_USER");
```

其中authoritiesBuilder主要是用于配置每一部分资源访问所需要的权限,与loadUserByUsername所配置的权限一致

# 访问说明

### 默认登录页

auth提供测试的默认登录页面(不推荐正式环境使用),页面请求方法为GET,请求地址为/login

### 登录

登录必须使用POST请求,默认地址为/login.do(修改配置只可改变前端访问路径,请求还是有auth执行),必须携带用户名(默认参数名merchant_name)和密码(默认参数名merchant_pwd)两个参数

当响应码为00是为登录成功,并且同时会在cookie中set一个token字段,字段的值就是身份令牌

200001-用户名不能为空(未取到字段)

200002-密码不能为空(未取到字段)

200003-用户名密码不匹配(默认登录页前端传输的密码经过一次md5加密)

### 注销登录

注销登录也必须使用POST方法,默认注销地址/logout,该请求不需要任何参数

### 认证请求

在配置AuthConfigurerAdapter拦截请求时一定要将登录页,登录,注销等请求报告在Filter的拦截中,除以上请求,其余请求都需要有对应路径的权限才能访问改资源

在认证请求获取身份令牌时,首先会检测路径参数中是否有token_id字段(用于支持RESTFul请求),当没有token_id字段才会检测cookie中的token字段

异常响应码:

200004-用户没有访问该部分资源的权限

200005-用户没有登录或者身份令牌过期


完整示例
-----

```java
@WebFilter(urlPatterns = "/*")
public class AuthConfigFilter extends AuthConfigurerAdapter implements UserService {

    @Override
    protected void configure(AuthConfig config){
        config.formLoginBuilder()
                    .loginDo("/login.do")
                    .loginPage("/login")
                    .usernameParameter("merchant_name")
                    .passwordParameter("merchant_pwd")
                    .and()
                .logoutBuilder()
                    .logoutUrl("/logout")
                    .and()
                .authoritiesBuilder()
                    .authorities("/admin/*", "ROLE_ADMIN")
                    .authorities("/user/*", "ROLE_USER");
    }

    @Override
    protected UserService customUserService() {
        return this;
    }

    @Override
    public UserDetails loadUserByUsername(String s) {
        return mockUser(s);
    }

    /**
     * 正式使用的时候请把这部分内容更换成数据库内容
     * @param username 用户名
     * @return
     */
    private UserDetails mockUser(String username){
        DefaultUserDetails userDetails = new DefaultUserDetails();
        Set<String> authorities = new HashSet<>();
        if("admin".equals(username)){
            userDetails.setUid(1);
            userDetails.setUsername("admin");
            userDetails.setPassword("21232f297a57a5a743894a0e4a801fc3");
            authorities.add("ROLE_ADMIN");
            authorities.add("ROLE_USER");
            userDetails.setAuthorities(authorities);
            return userDetails;
        }else if("user".equals(username)){
            userDetails.setUid(2);
            userDetails.setUsername("user");
            userDetails.setPassword("ee11cbb19052e40b07aac0ca060c23ee");
            authorities.add("ROLE_USER");
            userDetails.setAuthorities(authorities);
            return userDetails;
        }else {
            return null;
        }
    }
}
```



