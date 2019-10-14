from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, Regexp, EqualTo,\
    url, ValidationError

from .models import User


class LoginForm(Form):
    uname = StringField('Your Username:', validators=[DataRequired()])
    pword = PasswordField('Password', validators=[DataRequired()])
    p2fa = PasswordField('2fa',id="2fa", validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    result = StringField('Message')
    submit = SubmitField('Log In')

class TextForm(Form):
    inputtext = StringField('Your Text:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class RegisterForm(Form):
    uname = StringField('Username',
                    validators=[
                        DataRequired(), Length(3, 80),
                        Regexp('^[A-Za-z0-9_]{3,}$',
                            message='Usernames consist of numbers, letters,'
                                    'and underscores.')])
    pword = PasswordField('Password',
                    validators=[
                        DataRequired(),
                        EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    p2fa = PasswordField('2fa',id="2fa", validators=[DataRequired()])
    email = StringField('Email',
                        validators=[DataRequired(), Length(1, 120), Email()])

    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('There already is a user with this email address.')

    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('Incorrect - This username is already taken.')

