import os
import dotenv

base_dir = os.path.dirname(os.path.abspath(__file__))
env = os.path.join(base_dir, '.env')
dotenv.load_dotenv(env)

class BasicConfig:
    HOST=os.getenv('FLASK_HOST')
    PORT=os.getenv('FLASK_PORT')
    DEBUG=os.getenv('FLASK_DEBUG')

class MySQLConfig:
    def __init__(self):
        self.host = os.getenv('MYSQL_HOST')
        self.port = os.getenv('MYSQL_PORT')
        self.username = os.getenv('MYSQL_USERNAME')
        self.password = os.getenv('MYSQL_PASSWORD')
        self.database = os.getenv('MYSQL_DB')
    @property
    def SQLALCHEMY_DATABASE_URI(self):
        return f"mysql+pymysql://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

class SocketConfig:
    pass

class JWTConfig:
    JWT_SECRET_KEY=os.getenv('FLASK_SECRET_KEY')

