```java
File file = File.createTempFile("temp", ".png");
```

### 单例模式

```java
public class Signaleton {

    private Signaleton(){}

    private static class SingletonHolder{
        private static final Signaleton signaleton = new Signaleton();
    }
    
    public static Signaleton getInstance(){
        return SingletonHolder.signaleton;
    }
}
```