from sqlalchemy import create_engine
from urllib.parse import quote_plus

user = "user"
password = "Skein@2020"
encoded_password = quote_plus(password)
DATABASE_URL = f'mysql://{user}:{encoded_password}@demo.emeetify.com/turf_management'

# Create the engine
engine = create_engine(DATABASE_URL)
