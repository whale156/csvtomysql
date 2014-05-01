#!/usr/bin/env python3.3
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: csvtotable.py
#         Desc: usage: python3.3 csvtotable.py csv_table db_name db_table
#               ps: db_table must have same as field with csv
#       Author: Hugo
#        Email: 
#     HomePage: http://hugo-linuxs.blogspot.tw/
#      Version: 0.0.1
#   LastChange: 2014-04-27 22:18:35
#      History:
#=============================================================================

import sys, os
import pymysql
from fileread import csvread

sql_name = ""
sql_var  = ""

if(len(sys.argv) < 4):
    print("Usage: python3.3 csv_table db_name db_table ")
    sys.exit(1)

# 測試檔案是否存在
if not os.path.exists(sys.argv[1]):
    print("ERROR: File " +  sys.argv[1] + " was not found!")
    sys.exit(1)


# 測試 db 是否存在
try:
    db = pymysql.connect(host="localhost", user="root", passwd="", db= sys.argv[2], charset="utf8")
    cursor = db.cursor()

except:
    print("ERROR: db " + sys.argv[2] + "does not exist.")
    sys.exit(1)


# 測試 db_table 是否存在db 中
sql = "desc " + sys.argv[3]

try:

    cursor.execute(sql)
    field = cursor.fetchall()

    for i in range(len(field)):

        if(i < len(field)-1):
            sql_name = sql_name + field[i][0] + ", "
            sql_var  = sql_var + "'%s', "
        else: 
            sql_name = sql_name + field[i][0] 
            sql_var  = sql_var + "'%s'"

except :
    print("ERROR: db_dbtable " + sys.argv[3] + " does not exist.")
    sys.exit(1)



# read csv
csvread = csvread()
data = csvread.read(sys.argv[1])

for each in data:
    sql_data = str(each).replace("[","").replace("]","")

    try:
        sql = "insert into " + sys.argv[3] + "(" + sql_name + ") values (" + sql_data  + ");" 

        print(sql)
        cursor.execute(sql)
        print("insert ", each, "to db")

    except EOFError as e:
        print(e)

db.commit()
db.close()

