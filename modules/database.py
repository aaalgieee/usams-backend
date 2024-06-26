from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os
import sqlalchemy

load_dotenv()
DB_URL = "mariadb+pymysql://dev:@localhost:3306/usams"

engine = sqlalchemy.create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
