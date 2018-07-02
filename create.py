import os
from flask import Flask, render_template, request
from module1 import *

app = Flask(__name__)
app.config["SQLAlCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db.initapp(app)

def main():
    db.create_all


if __name__ = "__main__"
    with app.app_context():
        main()



