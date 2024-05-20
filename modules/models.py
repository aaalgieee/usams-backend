import sqlalchemy
from pydantic import BaseModel

from .database import Base

# class Account(Base):
#     __tablename__ = "account"
#     account_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
#     firstname = sqlalchemy.Column(sqlalchemy.String)
#     lastname = sqlalchemy.Column(sqlalchemy.String)
#     middlename = sqlalchemy.Column(sqlalchemy.String)
#     username = sqlalchemy.Column(sqlalchemy.String, unique=True)
#     password = sqlalchemy.Column(sqlalchemy.String)
#     def verify_password(self, password: str) -> bool:
#         # Add your password verification logic here
#         return self.password == password

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

class StatuscodeGroup(Base):
    __tablename__ = 'statuscode_group'
    statuscode_group_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
    table_name = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    range_start = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    range_end = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)

class Statuscode(Base):
    __tablename__ = 'statuscode'
    statuscode_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    label = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    statuscode_group_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('statuscode_group.statuscode_group_id'), nullable=False)

class Activity(Base):
    __tablename__ = 'activity'
    activity_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    semester_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    code = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    label = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text)
    location = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    college_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    activity_start_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    activity_end_date = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    activity_status = sqlalchemy.Column(sqlalchemy.Enum('active', 'inactive'), default='active')
    approved_by = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("account.account_id"))
    approved_date = sqlalchemy.Column(sqlalchemy.DateTime)
    disapproved_by = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("account.account_id"))
    disapproved_reason = sqlalchemy.Column(sqlalchemy.Text)
    disapproved_date = sqlalchemy.Column(sqlalchemy.DateTime)
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    datetime_updated = sqlalchemy.Column(sqlalchemy.DateTime)
    statuscode = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("statuscode.statuscode_id"))
    # statuscode_rel = sqlalchemy.orm.relationship('Statuscode')

# class Activity(Base):
#     __tablename__ = "activity"
#     activity_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, index=True)
#     account_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("account.account_id"))
#     activity = sqlalchemy.Column(sqlalchemy.String)
#     date = sqlalchemy.Column(sqlalchemy.Date)
#     time = sqlalchemy.Column(sqlalchemy.Time)
#     account = sqlalchemy.orm.relationship("Account", back_populates="activity")

class TransactionType(Base):
    __tablename__ = 'transaction_type'
    transaction_type_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    label = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)

class Role(Base):
    __tablename__ = 'role'
    role_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    label = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text)
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)

class AccountRole(Base):
    __tablename__ = 'account_role'
    account_role_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    account_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('account.account_id'), nullable=False)
    role_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('role.role_id'), nullable=False)
    granter_account = sqlalchemy.Column(sqlalchemy.Integer)
    account = sqlalchemy.orm.relationship('Account')
    role = sqlalchemy.orm.relationship('Role')

class AccountSession(Base):
    __tablename__ = 'account_session'
    account_session_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    account_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('account.account_id'), nullable=False)
    session_key = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    ip = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    datetime_last_request = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    account = sqlalchemy.orm.relationship('Account')

class Attendance(Base):
    __tablename__ = 'attendance'
    attendance_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    activity_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('activity.activity_id'), nullable=False)
    activity_code = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    card_id = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    student_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    employee_id = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    student_number = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    transaction_type_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('transaction_type.transaction_type_id'), nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('account.account_id'), nullable=False)
    ip_address = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    datetime_created = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    date_created = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    activity = sqlalchemy.orm.relationship('Activity')
    transaction_type = sqlalchemy.orm.relationship('TransactionType')
    user = sqlalchemy.orm.relationship('Account')

class EventLog(Base):
    __tablename__ = 'event_log'
    event_log_id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    account_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('account.account_id'), nullable=False)
    event_description = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    ip = sqlalchemy.Column(sqlalchemy.String(255), nullable=False)
    datetime_added = sqlalchemy.Column(sqlalchemy.DateTime, nullable=False)
    account = sqlalchemy.orm.relationship('Account')
