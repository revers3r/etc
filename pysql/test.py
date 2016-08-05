import pymysql.cursors
import logging

conn, cursor = 0, 0
class DBase(HOST, USER, PASS, DB, CHAR_SET):
	def __init__(self):
		global conn
		global cursor
		connection = pymysql.connect(host=HOST,
					user=USER,
					password=PASS,
					db=DB,
					charset=CHAR_SET)
		curs = connection.cursor()
		conn, cursor = connection, curs

	def select(self, query):
		curs.execute(query)
		rows = curs.fetchall()
		return rows

	def insert(self, query):
		curs.execute(query)
		return connection.commit()

	def crawl_init(self):
		sql = "CREATE TABLE original (url NVARCHAR(256), links VARCHAR(65536), hash VARCHAR(40));"
		curs.execute(sql)
        sql = "CREATE TABLE today (url NVARCHAR(256), links VARCHAR(65536), hash VARCHAR(40));"
        curs.execute(sql)
        sql = "CREATE TABLE suspicious (date BIGINT(5) UNSIGNED NOT NULL, url NVARCHAR(256), susp_link VARCHAR(65536), geoipes VARCHAR(16), virustotal_result BOOLEAN, malwr_result BOOLEAN);"
        curs.execute(sql)
        sql = "CREATE TABLE report (date BIGINT(5) UNSIGNED NOT NULL, url NVARCHAR(256), changed_links VARCHAR(1024), geoip VARCHAR(16));"
        curs.execute(sql)

    def close_db(self):
        try:
            connection.close()
            return True
        except:
            logging.warning("Database not open, yet.")
            return False

    def create_database(self, name):
        try:
            sql = "CREATE DATABASE %s" % name
            curs.execute(sql)
            return True
        except:
            logging.warning("Can't create database!!")
            return False

    def delete_data(self, table, column, value):
        try:
            sql = "DELETE FROM %s WHERE %s = \'%s\'" % (table, column, value)
            curs.execute(sql)
            return True
        except:
            logging.warning("Can't delete data from table!!")
            return False