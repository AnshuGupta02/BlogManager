from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# import sys
# import os.path
#
# sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
# TEMPLATE_DIR = os.path.abspath('../templates')
# STATIC_DIR = os.path.abspath('../static')
# , template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret hai kuchh bhi rkh lo'
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db=SQLAlchemy(app=app)

from routesCP import *

if __name__ == '__main__':
    app.debug=True
    app.run()
