from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask.cli import with_appcontext

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    nick = db.Column(db.String(6))
    pub_status = db.Column(db.Integer)
    articles = db.relationship('Articles', backref='publisher', lazy=True)

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)
    motto = db.Column(db.String(128))
    link1 = db.Column(db.String(16))
    link2 = db.Column(db.String(128))
    content = db.Column(db.Text, nullable=False)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)
    date_posted = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)
    date_pub = db.Column(db.DateTime)


@app.cli.command('create')
@with_appcontext  
def create_db():
  db.create_all()
  print('Database created!')
  return "Hello"

@app.cli.command('drop')
@with_appcontext
def drop_db():
  db.drop_all()
  print('Database dropped!')

if __name__ == "__main__":

    app.run(debug=True)
    raise SystemExit
