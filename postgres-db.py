import psycopg2    
conn = psycopg2.connect(database="red30",
	user="postgres",
	password="gayatri1",
	host="localhost",
	port="5432")
cur = conn.cursor()
cur.execute("select name,country from person")
print(cur.fetchall())
conn.close()