import pymysql

conn = pymysql.connect(host='localhost', user='root', password='toor',
                        db='member', charset='utf8')

curs = conn.cursor()
curs.execute("select * from user_table;")
rows = curs.fetchall()
print rows 