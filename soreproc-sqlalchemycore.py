from sqlalchemy import create_engine
from sqlalchemy import Table, MetaData

engine = create_engine('postgres://person:gayatri1@localhost/red30',
	isolation_level="AUTOCOMMIT")

with engine.connect() as connection:
	meta = MetaData(engine)
	person_table = Table('person', meta, autoload=True, autoload_with=engine)

	# connection.execute('COMMIT')
	connection.execute('CALL id (%s)', (2))
