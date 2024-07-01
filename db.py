import sqlite3

def get_db_connection():
	connection = sqlite3.connect("../db/sensor_data.db")
	connection.row_factory = sqlite3.Row
	return connection

def get_data(limit=50):
	connection = get_db_connection()
	limit_clause =  '' if limit == 'all' else ' limit ' + str(limit)
	sql_query =  'SELECT * FROM (SELECT * FROM sensor_data ORDER BY id DESC' + limit_clause + ') ORDER BY id ASC;'
	data = connection.execute(sql_query).fetchall()
	connection.close()
	return data
