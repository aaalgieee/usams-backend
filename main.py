from contextvars import Token
import os
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.hash import bcrypt
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# Database configuration
load_dotenv()
DB_URL = os.getenv("DB_URL")

engine = create_engine(DB_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database models
class Account(Base):
    __tablename__ = "account"
    account_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    firstname = sqlalchemy.Column(sqlalchemy.String)
    lastname = sqlalchemy.Column(sqlalchemy.String)
    middlename = sqlalchemy.Column(sqlalchemy.String)
    username = sqlalchemy.Column(sqlalchemy.String, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String)

app = FastAPI()

# Dependency function to get database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Endpoints
@app.get("/users")
def get_account(db: Session = Depends(get_db)):
    accounts = db.query(Account).all()
    return accounts

# Commented out code
# @app.post("/login", response_model=Token)
# async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = authenticate_user(db, form_data.username, form_data.password)

#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )

#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={"sub": user.username}, expires_delta=access_token_expires
#     )
#     return {"access_token": access_token, "token_type": "bearer"}