from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# from core.config import settings
load_dotenv()
username = os.environ.get('POSTGRES_USER')
password = os.environ.get('POSTGRES_PASSWORD')
dbase = os.environ.get('POSTGRES_DB')

SQLALCHEMY_DATABASE_URL = f'postgresql://{username}:{password}@localhost/{dbase}'
# SQLALCHEMY_DATABASE_URL = "postgresql://mzinzun:mzinzun@localhost/fastapi_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
