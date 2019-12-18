"""
    pymysql 数据库操作流程
"""
import pymysql
# 连接数据
db =pymysql.connect(host='localhost',
                    port=3306,
                    user='root',
                    password='123456',
                    database='school',
                    charset='utf8')
# 创建游标对象
cur =db.cursor()

# 利用游标对象执行 sql 语句

# 读操作 -》 fetch
# 写操作 -》 commit  rollback

# 关闭游标
cur.close()
# 关闭数据库
db.close()