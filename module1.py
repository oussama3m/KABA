from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()



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










    