from application import app, db
from application.forms import LoginForm, RegisterForm
from flask import render_template, request, redirect, flash, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash

@app.route("/")
@app.route("/home")
@app.route("/index")
def index():
    return render_template('index.html', home=True, title="Home")

@app.route("/dashboard")
def dashboard():
    if not session.get('username'):
        redirect(url_for('index'))

    with db.cursor() as cursor:
        cursor.execute("SELECT user.username, user.first_name, user.last_name, role.role_name FROM user, role WHERE user.role_id = role.role_id")
        users = cursor.fetchall()
        cursor.close()
        return render_template('dashboard.html', dashboard=True, users=users)

@app.route("/login", methods=["POST", "GET"])
def login():

    if session.get('username'):
        redirect(url_for('index'))

    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        with db.cursor() as cursor:
            password = loginForm.password.data
            cursor.execute(f'SELECT user.username, user.first_name, user.last_name, role.role_name, user.password FROM user, role WHERE user.role_id = role.role_id AND user.username = "{loginForm.username.data}"')
            auth = cursor.fetchone()
            cursor.close()
            if auth[0]:
                user = auth[0]
                if check_password_hash(user[4], password):
                    flash(f'Login request for user {loginForm.username.data}', "success")
                    session['username'] = user[0]
                    session['name'] = f'{user[1]} {user[2]}'
                    session['role'] = user[3]
                    return redirect('/dashboard')
                else:
                    flash("Your password is wrong")
            else:
                flash("Sorry something went wrong", "danger")
    return render_template('login.html', form=loginForm)

@app.route('/logout')
def logout():
    session['username'] = False
    session.pop('name', None)
    session.pop('role', None)
    return redirect(url_for('index'))

@app.route('/register', methods=["POST", "GET"])
def register():

    if session.get('username'):
        redirect(url_for('index'))

    registerForm = RegisterForm()
    if registerForm.validate_on_submit():
        username = registerForm.username.data
        first_name = registerForm.first_name.data
        last_name = registerForm.last_name.data
        password = registerForm.password.data

        hash_password = generate_password_hash(password)
        with db.cursor() as cursor:
            cursor.execute(f'INSERT INTO user(username, password, first_name, last_name, created_date, role_id) values ("{username}", "{hash_password}", "{first_name}", "{last_name}", NOW(), 2)')
            flash("You are successfully registered", "success")
            cursor.commit()
            cursor.close()
            return redirect(url_for('index'))
    
    return render_template('register.html', form=registerForm)
