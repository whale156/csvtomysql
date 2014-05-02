csvtomysql
==========

Use python3  transfer csvtable to mysql

usage: python3.3 csvtotable.py csv_table db_name db_table

ps: db_table must have same as field with csv


The test.csv in Mysql Table Structure

``` 
CREATE TABLE `test_table` (
      `name` varchar(6) NOT NULL PRIMARY KEY,
      `date` date NOT NULL,
      `num` double precision NOT NULL,
      `volume` integer NOT NULL
);
```
