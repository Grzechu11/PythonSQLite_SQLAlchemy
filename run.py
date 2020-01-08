# app.py - a minimal flask api using flask_restful
from flask import Flask, request
from flask_restplus import Resource, Api, fields, Namespace
from database.dbcontext import db_session, init_db


app = Flask(__name__)

api = Api(app, 
    version='1.0.0',
    title='Python API: Flask, swagger, SQLAlchemy',
    description='This is sample project to host Flask with swagger and SQLite (SQLAlchemy)',
    validate=True)

from endpoints.user_api import *

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == "__main__":
    print(app.url_map)
    init_db()
    app.run(debug=True, host='0.0.0.0')