import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(16)
    MYSQL_HOSTNAME = os.environ.get("MYSQL_HOSTNAME") or 'localhost'
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE')
    MYSQL_USERNAME = os.environ.get('MYSQL_USERNAME') or 'root'
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or ''