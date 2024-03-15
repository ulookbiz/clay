# Определение моделей
from datetime import datetime
from events import db

class Publisher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)  # название издателя
    nick = db.Column(db.String(6))  # короткий ник издателя
    pub_status = db.Column(db.Integer)  # статус издателя
    reference = db.Column(db.String(64))  # основная ссылка издателя
    emblem = db.Column(db.String(16))   # файл эмблемы
    articles = db.relationship('Articles', backref='author', lazy=True)  # отношение к статьям

    def __repr__(self):
        return f"Publisher('{self.id}', '{self.name}', '{self.nick}', '{self.emblem}')"

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
    images = db.relationship('Images', backref='article', lazy=True)  # отношение к изображениям

    def __repr__(self):
        return f"Articles('{self.title}', '{self.motto}', '{self.emblem}', '{date_posted}')"


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    i_name = db.Column(db.Integer)  # имя картинки - это просто число
    p_width = db.Column(db.Integer, nullable=False)    # ширина картинки
    p_height = db.Column(db.Integer, nullable=False)  # высота картинки
    articles_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)

    def __repr__(self):
        return f"Images('{self.i_name}'"
