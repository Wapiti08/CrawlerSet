'''
数据库代码
三张表
用户，历史，词典
'''
from pymysql import *

class mysqlpython:
    def __init__(self,host,user,pwd,charset="utf8"):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.charset=charset
    
    def open(self):
        self.conn=connect(host=self.host,user=self.user,passwd=self.pwd,charset=self.charset)
        self.cursor=self.conn.cursor()
    
    def run(self,sql):
        self.open()
        self.cursor.execute(sql)
        self.conn.commit()
        self.close()

    def close(self):
        self.cursor.close()
        self.conn.close()


pm=mysqlpython("localhost","root","")
sql="create database if not exists dict charset='utf8';\
     use dict;"
# pm.run(sql)
# sql="create table if not exists user(id int(3) zerofill,\
#             name varchar(20),\
#             passwd varchar(30),\
#             primary key(id),\
#             unique(name)\
#             );"
# sql="create table if not exists hist(\
#             id varchar(20),\
#             time Timestamp,\
#             word varchar(30),\
#             user_id
#         );"
# sql="create table if not exists words(id int(11),\
#             word varchar(30),\
#             interpret varchar(200));"
pm.run(sql)
