from application import app, db
from application.forms import LoginForm
from flask import render_template, request, redirect, flash

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html', home=True, title="Home")

@app.route("/dashboard")
def dashboard():
    with db.cursor() as cursor:
        cursor.execute("SELECT user.username, user.first_name, user.last_name, role.role_name FROM user, role WHERE user.role_id = role.role_id")
        users = cursor.fetchall()
        cursor.close()
        return render_template('dashboard.html', dashboard=True, users=users, title="Dashboard")

@app.route("/login", methods=["POST", "GET"])
def login():
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        with db.cursor() as cursor:
            cursor.execute(f'SELECT user.username, user.first_name, user.last_name, role.role_name FROM user, role WHERE user.role_id = role.role_id AND user.username = "{loginForm.username.data}" AND user.password = "{loginForm.password.data}"')
            auth = cursor.fetchone()
            if auth[0]:
                flash(f'Login request for user {loginForm.username.data}')
                return redirect('/dashboard')
    return render_template('login.html', loginForm=loginForm, title="Login")