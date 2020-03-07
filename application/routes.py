from application import app, db
from flask import render_template

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/dashboard")
def dashboard():
    return render_template('dashboard.html')
    