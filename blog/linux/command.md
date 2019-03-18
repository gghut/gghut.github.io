常用命令
====

```sh
chmod a+x file
```

* 添加可执行权限

```sh
chgrp -r <user> <filename>
chown -r <user> <filename>
```

* chgrp 修改文件/文件夹所属组群
* chown 修改文件/文件夹拥有者

```sh
find <dir> <arg> <model> [<arg> <model> ...]
find . -name '*.sh'
find / -perm 755
find -user root
find /home -mtime -5
find /home -mtime +3
find /ect -type l
find . -size +10000000c
```

* -name 按照名称查找
* -perm 按照属性查找
* -user 按照文件属主查找
* -mtime 按照文件更改时间查找,+为超过天数,-为指定天数以内
* -type 按照文件类型查找
* -size 按照文件大小查找

```sh
xargs
```

```sh
echo $JAVA_HOME
```

查看环境变量
