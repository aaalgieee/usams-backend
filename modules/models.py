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
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime)
    statuscode = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("status.statuscode_id"))
    emp_account = sqlalchemy.Column(sqlalchemy.Integer)

    def verify_password(self, password: str) -> bool:
        # Add your password verification logic here
        return self.password == password


class AccountRole(Base):
    __tablename__ = "account_role"
    account_role_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    account_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("account.account_id"))
    role = sqlalchemy.Column(sqlalchemy.String)
    granter_account = sqlalchemy.Column(sqlalchemy.String)


class Account_Session(Base):
    __tablename__ = "account_session"
    account_session_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    account_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("account.account_id"))
    session_key = sqlalchemy.Column(sqlalchemy.String)
    ip_address = sqlalchemy.Column(sqlalchemy.String)
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime)
    datetime_last_request = sqlalchemy.Column(sqlalchemy.DateTime)


class Activity(Base):
    __tablename__ = "activity"
    activity_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    semester_id = sqlalchemy.Column(sqlalchemy.Integer, )
    code = sqlalchemy.Column(sqlalchemy.String)
    label = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    location = sqlalchemy.Column(sqlalchemy.String)
    college_id = sqlalchemy.Column(sqlalchemy.Integer)
    activity_start_date = sqlalchemy.Column(sqlalchemy.Date)
    activity_end_date = sqlalchemy.Column(sqlalchemy.Date)
    activity_status = sqlalchemy.Column(sqlalchemy.Enum('Active', 'Inactive'))
    approved_by = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("account.account_id"))
    approved_date = sqlalchemy.Column(sqlalchemy.Date)
    disapproved_date = sqlalchemy.Column(sqlalchemy.Date)
    disapproved_by = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("account.account_id"))
    disapprove_reason = sqlalchemy.Column(sqlalchemy.String)
    disapprove_datetime = sqlalchemy.Column(sqlalchemy.DateTime)
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime)
    datetime_updated = sqlalchemy.Column(sqlalchemy.DateTime)
    statuscode = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("status.statuscode_id"))


class Attendance(Base):
    __tablename__ = "attendance"
    attendance_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    activity_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("activity.activity_id"))
    activity_code = sqlalchemy.Column(sqlalchemy.String)
    card_id = sqlalchemy.Column(sqlalchemy.String)
    student_id = sqlalchemy.Column(sqlalchemy.Integer)
    employee_id = sqlalchemy.Column(sqlalchemy.Integer)
    student_number = sqlalchemy.Column(sqlalchemy.String)
    transaction_type_id = sqlalchemy.Column(sqlalchemy.Integer,
                                            sqlalchemy.ForeignKey("transaction_type.transaction_type_id"))
    user_id = sqlalchemy.Column(sqlalchemy.Integer)
    ip_address = sqlalchemy.Column(sqlalchemy.String)
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime)
    date_created = sqlalchemy.Column(sqlalchemy.Date)


class EventLog(Base):
    __tablename__ = "event_log"
    event_log_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    account_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("account.account_id"))
    event_description = sqlalchemy.Column(sqlalchemy.String)
    ip_address = sqlalchemy.Column(sqlalchemy.String)
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime)


class Role(Base):
    __tablename__ = "role"
    role_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    label = sqlalchemy.Column(sqlalchemy.String)
    description = sqlalchemy.Column(sqlalchemy.String)
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime)


class Statuscode(Base):
    __tablename__ = "statuscode"
    statuscode_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    label = sqlalchemy.Column(sqlalchemy.String)
    statuscode_group_id = sqlalchemy.Column(sqlalchemy.Integer,
                                            sqlalchemy.ForeignKey("statuscode_group.statuscode_group_id"))


class StatuscodeGroup(Base):
    __tablename__ = "statuscode_group"
    statuscode_group_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    table_name = sqlalchemy.Column(sqlalchemy.String)
    range_start = sqlalchemy.Column(sqlalchemy.String)
    range_end = sqlalchemy.Column(sqlalchemy.String)


class TransactionType(Base):
    __tablename__ = "transaction_type"
    transaction_type_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    label = sqlalchemy.Column(sqlalchemy.String)
