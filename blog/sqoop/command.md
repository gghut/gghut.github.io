sqoop command
===

[官方文档 1.4.7](http://sqoop.apache.org/docs/1.4.7/SqoopUserGuide.html)

```sh
sqoop import \
--connect jdbc:mysql://localhost/userdb \
--username <username> \
--password <pwd> \
--table <table name> \
--m 1 \
--target-dir /dir \
--where <condition> \
--incremental <mode> \
--check-column <column name> \
--last-value <last check column value> \
--hive-import \
--create-hive-table \
--hive-talbe <table name> \
--fields-terminated-by <separator> \
--lines-terminated-by <separator> 
```

* import RDBMS向HDFS导入
* connect 数据库链接地址
* username 数据库账户
* password 数据库密码
* table 数据库表
* m
* target-dir 导入的目标文件夹
* where 表中的子集
* incremental
* check-column
* last-value
* hive-import 将数据导入到hive
* create-hive-table 自动创建表(如果表存在会报错)
* hive-table 自动创建表的名称
* fields-terminated-by 设置行内分割符号,hive默认行内分隔符"\0001"对应ASCII中的1,sqoop默认行内分割符","
* lines-terminated-by 行间分隔符

```sh
sqoop import-all-tables (generic-args) (import-args)
```

* 导入数据库中所有表

```sh
sqoop export
--connect jdbc:mysql://localhost/db \
--username <username> \
--password <pwd> \
--table <table name> \
--export-dir /emp/emp_data
--update-mode [allowinsert/updateonly]
--update-key <key name>
--input-fields-terminated-by <separator>
```

* export 从HDFS导出回RDBMS
* export-dir

```sh
sqoop list-databases (generic-args) (list-databases-args)
```

```sh
sqoop list-tables (generic-args) (list-tables-args)
```
