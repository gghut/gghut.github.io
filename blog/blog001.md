全半角转换
=====

* 全角:指一个字符占用两个标准字符位置。汉字字符和规定了全角的英文字符及国标GB2312-80中的图形符号和特殊字符都是全角字符。一般的系统命令是不用全角字符的，只是在作文字处理时才会使用全角字符。
* 半角:指一字符占用一个标准的字符位置。通常的英文字母、数字键、符号键都是半角的，半角的显示内码都是一个字节。在系统内部，以上三种字符是作为基本代码处理的。

unicode编码范围
----

* 空格:全角为12288（0x3000），半角为 32（0x20）
* 半角:33~126（0x21~0x7E）
* 全角:65281~65374（0xFF01~0xFF5E）

JAVA CODE DEMO
-----

全角转半角:

```java
    public String full2Half(String string) {
        char[] charArray = string.toCharArray();
        for (int i = 0; i < charArray.length; i++) {
            if (charArray[i] >= 65281 && charArray[i]  <= 65374) {
                charArray[i] = (char) (charArray[i] - 65248);
            }
        }
        return new String(charArray);
    }
```

半角转全角:

```java
    public String half2Full(String value) {
        char[] charArray = value.toCharArray();
        for (int i = 0; i < charArray.length; i++) {
            if (charArray[i] == 32) {
                charArray[i] = (char) 12288;
            } else if (charArray[i] < 127) {
                charArray[i] = (char) (charArray[i] + 65248);
            }
        }
        return new String(charArray);
    }
```