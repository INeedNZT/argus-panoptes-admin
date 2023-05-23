from sqlalchemy.dialects.mysql import BIGINT
from sqlalchemy import ForeignKey
from . import db

class Event(db.Model):
    __tablename__ = 'ap_events'
    id = db.Column(BIGINT(unsigned=True), primary_key=True, autoincrement=True)
    event_msg = db.Column(db.String(45), nullable=False)
    event_thumb = db.Column(db.String(45))
    event_video = db.Column(db.String(45))
    risk_level = db.Column(db.Integer, nullable=False, comment='event risk: 1 - low, 2 - medium, 3 - critical')
    email_sent = db.Column(db.Integer, nullable=False, default=0)
    sms_sent = db.Column(db.Integer, nullable=False, default=0)
    create_by = db.Column(db.String(45), ForeignKey('ap_monitors.id'), nullable=False, comment='the id of monitor which create this event')
    create_date = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())