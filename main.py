from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import DATE
from sqlalchemy.orm import Session

from sqlalchemy.sql import func, cast
from modules import models
from modules.database import SessionLocal, engine
from modules.models import Account, Activity, Attendance, Students, Statuscode
from pydantic import BaseModel, Field
from datetime import date, datetime, time
from typing import List


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
    activity_id: Optional[int]
    # semester_id: Optional[int]
    #code: str
    label: str
    department: str
    location: str
    # college_id: Optional[int]
    activity_start_date: date
    activity_end_date: date
    activity_status: Optional[str] = Field(default="inactive")
    #datetime_created: Optional[datetime] = Field(default=datetime.now())
    # approved_by: Optional[int]

class Students(BaseModel):
    student_number: int
    lastname: str
    firstname: str
    middlename: Optional[str]

class _Attendance(BaseModel):
    attendance_id: Optional[int]
    student_number: int
    activity_id: int
    datetime_created: datetime = Field(default=datetime.now())


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

    # Increment activity_id
    last_activity = db.query(Activity).order_by(Activity.activity_id.desc()).first()
    if last_activity:
        activity.activity_id = last_activity.activity_id + 1
    else:
        activity.activity_id = 1

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
    attendance = db.query(Attendance).filter(Attendance.activity_id == activity_id).first()
    if attendance:
        db.delete(attendance)
    activity = db.query(Activity).filter(Activity.activity_id == activity_id).first()
    if not activity:
        raise HTTPException(status_code=404, detail="Event not found")
    db.delete(activity)
    db.commit()
    return {"message": "Event deleted"}


@app.get("/reports/{activity_id}")
def get_attendance(activity_id: int, db: Session = Depends(get_db)):
    attendance = db.query(models.Attendance, models.Students, models.Activity)\
        .join(models.Students)\
        .join(models.Activity)\
        .filter(models.Attendance.activity_id == activity_id)\
        .all()
    
    attendance_details = []
    for record in attendance:
        attendance_details.append({
            "attendance_id": record.Attendance.attendance_id,
            "activity_id": record.Attendance.activity_id,
            "student_number": record.Attendance.student_number,
            "datetime_created": record.Attendance.datetime_created,
            "firstname": record.Students.firstname,
            "lastname": record.Students.lastname,
            "activity_label": record.Activity.label
        })
    return attendance_details




@app.post("/attendance")
def add_attendance(att: _Attendance, db: Session = Depends(get_db)):
    # Check if attendance for the same activity and date already exists
    today = datetime.now().date()
    existing_attendance = db.query(Attendance).filter(
        Attendance.activity_id == att.activity_id,
        cast(Attendance.datetime_created, DATE) == today,
        Attendance.student_number == att.student_number
    ).first()
    
    if existing_attendance:
        return {"message": "Attendance already registered for this activity today"}

    attendance = Attendance(
        student_number=att.student_number, 
        activity_id=att.activity_id, 
        datetime_created=datetime.now()
    )

    # Increment attendance_id
    last_attendance = db.query(Attendance).order_by(Attendance.attendance_id.desc()).first()
    if last_attendance:
        attendance.attendance_id = last_attendance.attendance_id + 1
    else:
        attendance.attendance_id = 1

    db.add(attendance)
    db.commit()

    log_event(db, 0, f"Added attendance for activity {att.activity_id}", "")
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
