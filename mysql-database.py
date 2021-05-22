import mysql.connector as mysql
from mysql.connector import cursor
from mysql.connector.errors import Error

def connect(db_name):
	try:
		return mysql.connect(
			host='localhost',
			user='root',
			password='gayatri1',
			database=db_name)
	except Error as e:
		print(e)

if __name__ == '__main__':
	db = connect("project")
	cursor = db.cursor()

	cursor.execute("SELECT * FROM project")
	project_records = cursor.fetchall()
	print(project_records)

	db.close()