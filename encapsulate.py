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

def add_new_project(cursor, project_title, project_description, 
	task_descriptions):
	project_data = (project_title, project_description)
	cursor.execute('''INSERT INTO task1(title, description) 
		VALUES (%s, %s)''', project_data)

	p_id = cursor.lastrowid

	tasks_data = []

	for description in task_descriptions:
		task_data = (p_id, description)
		tasks_data.append(task_data)

	cursor.executemany('''INSERT INTO project(p_name, description)
		VALUES (%s, %s)''', tasks_data)

if __name__ == '__main__':
	db = connect("task1")
cursor = db.cursor()

task1 = ["Clean bathroom", "Clean kitchen", "Clean living room"]
add_new_project(cursor, "Clean house", "Clean house by room", task1)
db.commit()

cursor.execute("SELECT * FROM task1")
project_records = cursor.fetchall()
print(project_records)
cursor.execute("SELECT * FROM project")
tasks_records = cursor.fetchall()
print(tasks_records)

db.close()





