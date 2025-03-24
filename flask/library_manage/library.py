from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/flask_library"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Member(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(100))
    phone = db.Column(db.String(13))

with app.app_context():
    db.create_all()
    db.session.commit()

@app.route("/")
def index():
    members = Member.query.all()
    return render_template("index.html", members=members)

@app.route("/new")
def new():
    return render_template("form.html", form_action='insert', member=None)

@app.route("/insert", methods=["POST"])
def insert():
    firstname = request.form.get("first_name")
    lastname = request.form.get("last_name")
    email = request.form.get("email")
    phone = request.form.get("phone")
    
    # بررسی داده‌های ضروری
    errors = []
    if not firstname:
        errors.append("نام ضروری است!")
    if not lastname:
        errors.append("نام خانوادگی ضروری است!")
    
    if errors:
        return render_template("form.html", form_action='insert', member=None, errors=errors), 400
    
    new_member = Member(firstname=firstname, lastname=lastname, email=email, phone=phone)
    db.session.add(new_member)
    db.session.commit()
    
    return redirect(url_for('index'))

@app.route("/edit/<int:id>")
def edit(id):
    member = Member.query.get_or_404(id)
    return render_template('form.html', member=member, form_action='update')

@app.route('/update', methods=['POST'])
def update():
    id = request.form.get("id")
    member = Member.query.get_or_404(id)  # استفاده از get_or_404 برای یکنواختی
    
    member.firstname = request.form.get("first_name")
    member.lastname = request.form.get("last_name")
    member.email = request.form.get("email")
    member.phone = request.form.get("phone")
    
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/delete/<int:id>")
def delete(id):
    member = Member.query.get_or_404(id)  # استفاده از get_or_404 برای یکنواختی
    
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)