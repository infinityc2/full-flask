from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Login')

class FilterForm(FlaskForm):
    username = StringField('Username'),
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    role = StringField('Role')
    submit = SubmitField('Filter')