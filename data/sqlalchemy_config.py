from sqlalchemy import create_engine

DATABASE_URI = 'mysql://root:mysqllocal@localhost/turfmanagement'

engine = create_engine(DATABASE_URI)