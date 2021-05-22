import psycopg2

if __name__ == "__main__":
	conn = psycopg2.connect(database="red30",
		user="postgres",
		password="gayatri1",
		host="localhost",
		port="5432")

	conn.autocommit = True
	
	cur = conn.cursor()

	cur.execute('''CALL id (%s)''',(2))
	
	# How to Call Postgres Function: 
	# cur.callproc('return_nondiscounted_item', (1105910, 1))

	conn.close()