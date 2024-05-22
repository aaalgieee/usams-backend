from sqlalchemy import Column, Integer, String, DateTime, func, cast, DATE
import sqlalchemy
from pydantic import BaseModel

from .database import Base


class Account(Base):
    __tablename__ = 'account'
    account_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    username = sqlalchemy.Column(sqlalchemy.String(255), nullable=False, unique=True)
    password = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    lastname = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    firstname = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    middlename = sqlalchemy.Column(sqlalchemy.String(255))
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    # statuscode = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('statuscode.statuscode'), nullable=False)
    # emp_account = sqlalchemy.Column(sqlalchemy.Integer)
    # statuscode_rel = sqlalchemy.orm.relationship('Statuscode')

    def verify_password(self, password: str) -> bool:
        # Add your password verification logic here
        return self.password == password


class Statuscode(Base):
    __tablename__ = 'statuscode'
    statuscode_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    label = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    #statuscode_group_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('statuscode_group.statuscode_group_id'), nullable=False)

class Activity(Base):
    __tablename__ = 'activity'
    activity_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    semester_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    code = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    label = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    department = sqlalchemy.Column(sqlalchemy.String(255))
    location = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    college_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    activity_start_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    activity_end_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    activity_status = sqlalchemy.Column(sqlalchemy.Enum('active', 'inactive'), default='inactive')
    approved_by = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("account.account_id"))
    approved_date = sqlalchemy.Column(sqlalchemy.DateTime)
    disapproved_by = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("account.account_id"))
    disapproved_reason = sqlalchemy.Column(sqlalchemy.Text)
    disapproved_date = sqlalchemy.Column(sqlalchemy.DateTime)
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    datetime_updated = sqlalchemy.Column(sqlalchemy.DateTime)
    statuscode = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("statuscode.statuscode_id"))


class Attendance(Base):
    __tablename__ = 'attendance'
    attendance_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    activity_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('activity.activity_id'), nullable=False)
    student_number = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('students.student_number'), nullable=False)
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    

class Students(Base):
    __tablename__ = 'students'
    student_number = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    lastname = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    firstname = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    middlename = sqlalchemy.Column(sqlalchemy.String(255))