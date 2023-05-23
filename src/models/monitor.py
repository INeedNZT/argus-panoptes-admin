from sqlalchemy.dialects.mysql import BIGINT
from . import db

class Monitor(db.Model):
    __tablename__ = 'ap_monitors'
    id = db.Column(db.String(45), primary_key=True)
    monitor_sn =  db.Column(db.String(45), unique=True)
    monitor_name = db.Column(db.String(45), nullable=False)
    monitor_brand = db.Column(db.String(45))
    last_login = db.Column(db.DateTime)
    create_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())