from sqlalchemy import create_engine

DATABASE_URL = 'mysql://root:mysqllocal@localhost/turfmanagement'

engine = create_engine(DATABASE_URL)  