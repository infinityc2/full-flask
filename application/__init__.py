from flask import Flask
import pymysql

app = Flask(__name__)
db = pymysql.connect("localhost", "root", "accident1", "python_db")

from application import routes
