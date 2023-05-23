import logging
from ..models.log import Log

def get_logger(db):
    logger = logging.Logger('apa_logger')
    logger.setLevel(logging.DEBUG)
    logger.addHandler(MySQLHandler(db))

    return logger

class MySQLHandler(logging.Handler):
    """
    MySQL的logging实现, 继承了logging.Handler,
    重写了emit函数, 将日志输出到表ap_logs表中
    写入日志的字段 (详见logging.LogRecord):
        msg
        levelno
        levelname
        filename
        funcName
        #### 额外的字段 ####
        user_id
        monitor_id
        create_date
    """

    def __init__(self, db):
        super().__init__()
        self.db = db

    def emit(self, record):
        log = Log(msg=record.msg, levelno=record.levelno, levelname=record.levelname,
                  filename=record.filename, funcName=record.funcName)
        self.db.session.add(log)
        self.db.session.commit()
