修改用户秘密
====

```sql
alter user user identified by  '123456';
alter user user() identified by '123456';
alter user user identified by '123456' password expire;
alter user user identified by '123456' password expire never;
```