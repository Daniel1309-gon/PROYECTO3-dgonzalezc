from flask import Flask
from db import db
from flask_restful import Api
import os
import pymysql
pymysql.install_as_MySQLdb()


app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://{os.getenv("USER_DB")}:{os.getenv("PASSWORD_DB")}@{os.getenv("HOST_DB")}/{os.getenv("SCHEMA_DB")}'
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql://root:OVujqWZiWglwoiuirdlJIZpqDAzbYshk@roundhouse.proxy.rlwy.net:37899/railway'
db.init_app(app)
api = Api(app)
