#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost","root","root","python" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

'''
#SQL insert
sql="INSERT INTO student(name,class,grade) VALUES('laoluo','math',60),('laoluo','chinese',61),('laoluo','english',62);"

try:
	#execute sql
	cursor.execute(sql)
	#submit data to db
   	db.commit()
except:
	#rollback when occur a error
	db.rollback();
'''

sql="SELECT * FROM student"
	WHERE grade >  


# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取一条数据库。
data = cursor.fetchone()

print "Database version : %s " % data

# 关闭数据库连接
db.close()
