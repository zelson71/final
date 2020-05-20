from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:localhost@localhost/wines_db'

@app.route("/")
def wine():
    return render_template("index.html")

@app.route("/next")
def next():
    return render_template("next.html")

if __name__ == "__main__":
    app.run(debug=True)
