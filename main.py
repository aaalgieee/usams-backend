from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from modules import models
from modules.database import SessionLocal, engine
from modules.models import Account, Activity, Attendance, EventLog
from pydantic import BaseModel, Field
from datetime import date, datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
from fastapi import Request

@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    response = await call_next(request)
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

# Dependency function to get database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

def log_event(db: Session, account_id: int, event_description: str, ip: str):
    try:
        event = EventLog(account_id=account_id, event_description=event_description, ip=ip, datetime_added=datetime.now())
        db.add(event)
        db.commit()
    except Exception as e:
        db.rollback()

        # passively ignore error
        pass

# Endpoints
@app.get("/test/users")
def get_account(db: Session = Depends(get_db)):
    accounts = db.query(Account).all()
    return accounts

class Users(BaseModel):
    username: str
    password: str
    firstname: str
    lastname: str

class User(BaseModel):
    username: str
    password:str

class Event(BaseModel):
    # activity_id: Optional[int]
    # semester_id: Optional[int]
    #code: str
    label: str
    # description: Optional[str]
    location: str
    # college_id: Optional[int]
    activity_start_date: date
    activity_end_date: date
    activity_status: Optional[str] = Field(default="Active")
    datetime_created: Optional[datetime] = Field(default=datetime.now())
    # approved_by: Optional[int]

@app.post("/login")
def login(user: User, db: Session = Depends(get_db)):
    account = db.query(Account).filter(Account.username == user.username).first()
    if not account or not account.verify_password(user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Login successful"}

@app.post("/register")
def register(user: Users, db: Session = Depends(get_db)):
    account = Account(**user.dict())
    db.add(account)
    db.commit()
    return {"message": "Registration successful"}

@app.get("/events")
def get_events(db: Session = Depends(get_db)):
    events = db.query(Activity).all()
    return events

@app.post("/events")
def add_event(evt: Event, db: Session = Depends(get_db)):
    activity = Activity(**evt.dict())
    # add approved_by default admin user to activity
    activity.approved_by = 1

    db.add(activity)
    db.commit()
    return {"message": "Event added"}

@app.patch("/events/{activity_id}")
def update_event(activity_id: int, activity: Event, db: Session = Depends(get_db)):
    db.query(Activity).filter(Event.activity_id == activity_id).update(activity.dict())
    db.commit()
    return {"message": "Event updated"}

@app.delete("/events/{activity_id}")
def delete_event(activity_id: int, db: Session = Depends(get_db)):
    activity = db.query(Activity).filter(Activity.activity_id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(activity)
    db.commit()
    return {"message": "Event deleted"}

@app.get("/attendance")
def get_attendance(db: Session = Depends(get_db)):
    attendance = db.query(Attendance).all()
    return attendance

class _Attendance(BaseModel):
    activity_id: int
    account_id: int
    attendance_status: str = Field(default="Present")
    datetime_created: datetime = Field(default=datetime.now())

@app.post("/attendance")
def add_attendance(att: _Attendance, db: Session = Depends(get_db)):
    attendance = Attendance(**att.dict())
    db.add(attendance)
    db.commit()

    log_event(db, att.account_id, f"Added attendance for activity {att.activity_id}", "")
    return {"message": "Attendance added"}

@app.patch("/attendance/{attendance_id}")
def update_attendance(attendance_id: int, att: _Attendance, db: Session = Depends(get_db)):
    db.query(Attendance).filter(Attendance.attendance_id == attendance_id).update(att.dict())
    db.commit()

    log_event(db, att.account_id, f"Updated attendance for activity {att.activity_id}", "")
    return {"message": "Attendance updated"}

@app.delete("/attendance/{attendance_id}")
def delete_attendance(attendance_id: int, db: Session = Depends(get_db)):
    attendance = db.query(Attendance).filter(Attendance.attendance_id == attendance_id).first()
    if not attendance:
        raise HTTPException(status_code=404, detail="Attendance not found")
    db.delete(attendance)
    db.commit()

    log_event(db, attendance.account_id, f"Deleted attendance for activity {attendance.activity_id}", "")
    return {"message": "Attendance deleted"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", port=8000, reload=True)
