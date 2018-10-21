import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '2cf6f26d05281dd899b5fd80a648becfe9c1fa7f9a593437'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'proto.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False