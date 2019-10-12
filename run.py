from datetime import datetime
from flask import Flask, render_template, request, flash, redirect, url_for

from .forms import LoginForm, RegisterForm, TextForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '~t\x86\xc9\x1ew\x8bOcX\x85O\xb6\xa2\x11kL\xd1\xce\x7f\x14<y\x9e'


@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()

    return render_template("register.html", form=form)



@app.route("/login", methods=["GET", "POST"])
def login():
	form = LoginForm()
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

