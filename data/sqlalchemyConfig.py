from sqlalchemy import create_engine

DATABASE_URL = 'mysql://user:Skein@2020@demo.emeetify.com/turf_management'

engine = create_engine(DATABASE_URL)  