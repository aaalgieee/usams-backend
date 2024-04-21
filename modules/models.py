import sqlalchemy
from pydantic import BaseModel

from .database import Base

class Account(Base):
    __tablename__ = "account"
    account_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    firstname = sqlalchemy.Column(sqlalchemy.String)
    lastname = sqlalchemy.Column(sqlalchemy.String)
    middlename = sqlalchemy.Column(sqlalchemy.String)
    username = sqlalchemy.Column(sqlalchemy.String, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String)
    def verify_password(self, password: str) -> bool:
        # Add your password verification logic here
        return self.password == password
    

class User(BaseModel):
    username: str
    password: str