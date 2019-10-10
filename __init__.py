import os

from flask import Flask

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

