from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
# app.config["SQLALCHEMY_DATABASE_MODIFICATIONS"] = False

db = SQLAlchemy(app)





class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"





@app.route('/')
def hello_world():
    return render_template('index.html')
    # return 'Hello, World!'


@app.route('/khushi')
def prod():
    return 'this is another api endpoint'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        print("checking statement")
    app.run(debug=True, port=8000)
