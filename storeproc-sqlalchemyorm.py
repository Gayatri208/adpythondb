from sqlalchemy import create_engine, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgres://postgres:gayatri1@localhost/red30')
#isolation_level="AUTOCOMMIT"

Base = declarative_base(engine)
Base.metadata.reflect(engine)

class Sales(Base):
	__table__ = Base.metadata.tables['person']

	def __repr__(self):
		return '''<Sale(name='{0}',country='{1}'>'''.format(self.name, 
				self.country)

if __name__ == "__main__":
	with engine.connect() as connection:
		connection.execute("COMMIT")
		connection.execute('CALL id(%s)', (3))
		