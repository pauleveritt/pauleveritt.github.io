from os.path import join, abspath

from flask import Flask, render_template, send_from_directory
from flask.ext.restless import APIManager
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, unique=True)


db.create_all()

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Todo, methods=['GET', 'POST', 'DELETE', 'PATCH'])

node_modules = abspath(join(app.root_path, '../node_modules'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/lib/<path:filename>')
def base_static(filename):
    return send_from_directory(node_modules, filename)
