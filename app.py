from flask import Flask
from flask_flatpages import FlatPages


app = Flask(__name__)
app.config.from_pyfile('settings.py')
pages = FlatPages(app)


from .views import *
