from flask import Flask
from config import Config
import pymysql

app = Flask(__name__)
app.config.from_object(Config)
db = pymysql.connect("localhost", "xxx", "xxx", "xxx")

from application import routes
