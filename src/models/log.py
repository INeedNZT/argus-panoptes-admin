from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy import ForeignKey
from . import db

class Log(db.Model):
    __tablename__ = 'ap_logs'
    id = db.Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    msg = db.Column(db.String(45))
    levelno = db.Column(db.Integer)
    levelname = db.Column(db.String(45))
    filename = db.Column(db.String(45))
    funcName = db.Column(db.String(45))
    user_id = db.Column(BIGINT(unsigned=True), ForeignKey('ap_users.id'), comment='the id of user if applicable')
    monitor_id = db.Column(db.String(45), ForeignKey('ap_monitors.id'), comment='the id of monitor if applicable') 
    create_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())