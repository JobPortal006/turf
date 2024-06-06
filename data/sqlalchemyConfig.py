from sqlalchemy import create_engine

DATABASE_URL = 'mysql://root:root123@localhost/turfmanagement'

engine = create_engine(DATABASE_URL)   