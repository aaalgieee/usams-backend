from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from modules import models
from modules.database import SessionLocal, engine
from modules.models import Account
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)

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

class User(BaseModel):
    username: str
    password: str

@app.post("/login")
def login(user: User, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.username == user.username).first()
    if not account or not account.verify_password(user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Login successful"}


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development, allow all origins (restrict in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)