import psycopg2

conn = psycopg2.connect(database="red30",
	user="postgres",
	password="gayatri1",
	host="localhost",
	port="5432")

cursor = conn.cursor()

cursor.execute('''INSERT INTO person(name,country) VALUES
 	( 'suhani','us'
)''')

# conn.commit()

cursor.execute("SELECT name,country from person")
print(cursor.fetchall())


conn.close()



