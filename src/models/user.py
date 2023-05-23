from sqlalchemy.dialects.mysql import BIGINT
from . import db

class User(db.Model):
    __tablename__ = 'ap_users'
    id = db.Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(45), nullable=False, unique=True)
    user_pwd = db.Column(db.String(45), nullable=False)
    user_email = db.Column(db.String(45))
    user_phone = db.Column(db.String(45))
    last_login = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())
    modify_date = db.Column(db.DateTime, onupdate=db.func.current_timestamp())