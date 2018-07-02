from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

import os

from flask import Flask, render_template, request


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    line_id = db.Column(db.Integer, db.ForeignKey("lines.id"), nullable=False)
    
    state = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String, nullable=True)
    quantity = db.Column(db.Integer, nullable=True)
    category = db.Column(db.String, nullable=True)
    


class Line(db.Model ):
    __tablename__ = "lines"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)



def main():
    db.create_all()
    a = Line(name="pc")
    db.session.add(a)
    b=Line.query.filter_by(id=1).all
    db.session.commit()
    
    print( "bb" )

@app.route("/")
def h():
    print("hello world")
    b=Line.query.filter_by(id=1).all
    return b


if __name__ == "__main__":
    with app.app_context():
        main()

    