from flask import Flask, render_template, request , redirect,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/flask2"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    comment = db.Column(db.String(1000))

@app.route('/')
def index():
    results = Comment.query.all()
    return render_template("index.html",results=results)

@app.route("/submit", methods=['GET', 'POST'])
def submit():
    return render_template("submit.html")

@app.route("/process", methods=['POST'])
def process():
    name = request.form['name']
    comment = request.form["comment"]
    
    user_comment = Comment(name=name,comment=comment)
    db.session.add(user_comment)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == '__main__':

    app.run(debug=True)
