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
    name = db.Column(db.String(64), nullable=False)  # название издателя
    nick = db.Column(db.String(6))  # короткий ник издателя
    pub_status = db.Column(db.Integer)  # статус издателя
    reference = db.Column(db.String(64))  # основная ссылка издателя
    emblem = db.Column(db.String(16))   # файл эмблемы
    articles = db.relationship('Articles', backref='publisher', lazy=True)  # отношение к статьям


class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), nullable=False)  # заголовок статьи
    motto = db.Column(db.String(128))  # особый девиз статьи
    ilink = db.Column(db.String(16))  # внутренняя ссылка статьи
    olink = db.Column(db.String(128))  # внешняя ссылка статьи
    content = db.Column(db.Text, nullable=False)  # содержание статьи
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)  # время записи в базу данных
    date_pub = db.Column(db.DateTime)  # оригинальная дата статьи
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'), nullable=False)
    images = db.relationship('Images', backref='articles', lazy=True)  # отношение к изображениям


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    i_name = db.Column(db.Integer)  # имя картинки - это просто число
    p_width = db.Column(db.Integer, nullable=False)    # ширина картинки
    p_height = db.Column(db.Integer, nullable=False)  # высота картинки
    articles_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)

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
