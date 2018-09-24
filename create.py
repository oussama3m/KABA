import os
from flask import Flask, render_template, request, session 
import requests
#from flask_session import Session
from module1 import *

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
app.config["SESSION_PERMANENT"]= False
app.config["SESSION_TYPE"]= "filesystem"
db.init_app(app)


def main():
    print("hi1")
    db.create_all()
    print("hi2")


def addLines():
    for i in range(5):
        name="line"+str(i)
        l=Line(name=name)
        db.session.add(l)

    db.session.commit()

def addArticles():
    for i in range(20):
        db.create_all()
        a=Article(name="artcile"+str(i), line_id=(i%5)+13)
        db.session.add(a)

    db.session.commit()

@app.route("/", methods=["GET" , "POST"])
def index():
 #   db.query
 #   results=Article.query.all()
    
    rate=0
    if request.method == "POST" :
        base=request.form.get("base")
        symbol=request.form.get("symbol")
        base = "usd"
        symbol = "eur"
        
        res=requests.get("http://api.fixer.io/latest", params={"base":base, "symbols":symbol})
        if res.status_code!=200:
            raise Exception("ERROR: API request was not successful")

        data=res.json()
        rate=data["rates"][symbol]

    
        


    results=db.session.query(Article , Line).filter( Line.id == Article.line_id).all()
    ids=db.session.query(Line).all()
    send=dict()
    send["rate"]=rate
    send["results"]=results
    send["ids"]=ids
    
    
    return render_template("index.html", send = send  )



@app.route("/admin")
def admin():
    if session.get("log") == None:
        session["log"]= True
    return render_template("admin.html")

@app.route("/add", methods=["GET" , "POST"])
def addArticle():

    if request.method == "POST":

        name = request.form.get("name")
        line_id = request.form.get("line_id")
        return render_template("form_desplay.html", name=name)
    
    else:
        return render_template("form_add.html")




# if __name__ == "__main__":
    
#     with app.app_context():
#         addArticles()

   



