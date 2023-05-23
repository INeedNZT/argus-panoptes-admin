from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy import ForeignKey
from . import db

class Token(db.Model):
    __tablename__ = 'ap_tokens'
    id = db.Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    monitor_id = db.Column(db.String(45), ForeignKey('ap_monitors.id'), comment='the id of monitor if applicable') 
    user_id = db.Column(BIGINT(unsigned=True), ForeignKey('ap_users.id'), comment='the id of user if applicable')
    token_val = db.Column(db.String(45), nullable=False)
    token_type = db.Column(db.Integer, nullable=False, comment='1 - monitor, 2 - user')
    block_status = db.Column(db.Integer, default=0)
    ip_address = db.Column(db.String(45))
    expire_date =  db.Column(db.DateTime, nullable=False)
    create_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())