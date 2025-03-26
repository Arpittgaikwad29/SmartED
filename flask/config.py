import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@localhost/teams_clone_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False