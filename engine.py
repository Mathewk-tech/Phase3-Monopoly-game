import os
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from dotenv import load_dotenv
from sqlalchemy.pool import NullPool

#this loads the variables from the .env file
load_dotenv()

db_credentials={
    "drivername": "postgresql+psycopg2",
    "username": os.getenv("DB_USERNAME"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "database": os.getenv("DB_NAME"),
}

DATABASE_URL=URL.create(**db_credentials)

engine=create_engine(DATABASE_URL,echo=False, poolclass=NullPool)