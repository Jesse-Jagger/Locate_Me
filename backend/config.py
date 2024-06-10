import os

class Config:
    SECRET_KEY = os.environ.get('you-will-never-guess')
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/locate_me_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_jwt_secret_key'