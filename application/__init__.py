from flask import Flask
from config import Config
import pymysql

app = Flask(__name__)
app.config.from_object(Config)
db = pymysql.connect(Config.MYSQL_HOSTNAME, Config.MYSQL_USERNAME, Config.MYSQL_PASSWORD, Config.MYSQL_DATABASE)

from application import routes
