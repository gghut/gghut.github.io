sqoop command
===

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
```

* export 从HDFS导出回RDBMS
* export-dir

```sh
sqoop list-databases (generic-args) (list-databases-args)
```

```sh
sqoop list-tables (generic-args) (list-tables-args)
```
