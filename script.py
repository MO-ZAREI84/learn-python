from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
     return "your welcome"

@app.route("/submit")
def submit():
     return "hhh submit"
if __name__ == '__main__':
    app.run(debug=True)