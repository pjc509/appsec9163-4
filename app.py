import os

from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
#from flask.ext.moment import Moment


basedir = os.path.abspath(os.path.dirname(__file__))


from .forms import LoginForm, RegisterForm, TextForm
from .models import User

app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'spellchecker.db')
db = SQLAlchemy(app)

# Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"
login_manager.init_app(app)



@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.uname.data,
                    password = form.pword.data)
        db.session.add(user)
        db.session.commit()
        flash('Success - Welcome, {}! Please login.'.format(user.username))
        #return redirect(url_for('login'))
        #return redirect(url_for('login'))
    return render_template("register.html", form=form)



@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.get_by_username(form.uname.data)
        if user is not None and user.check_password(form.pword.data):
            login_user(user, form.remember_me.data)
            flash("id=result Success - Logged in successfully as {}.".format(user.uname))
            return render_template('login.html', form=form)
        flash('id result Incorrect username or password.')
        return render_template('login.html', form=form)
    return render_template('login.html', form=form)


@app.route("/spell_check", methods=["GET", "POST"])
def spell_check():
    form = TextForm()
    return render_template("spell_check.html", form=form)



@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=False)

