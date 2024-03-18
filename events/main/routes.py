from flask import render_template, Blueprint, jsonify, render_template_string, request, redirect, url_for
from datetime import datetime
from ..content_generators.home_content import GetHomeContent
from ..content_generators.article_content import GetArticleContent
from ..content_generators.article_input import ArticleInput
from ..content_generators.publisher_content import GetPublisherContent
from ..content_generators.publisher_input import PublisherInput
from events import db, app
from movefiles import rename_and_move_files
from transform import transform

import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent.parent
sys.path.append(str(parent_dir))
from dbase.models import Publisher, Articles

main = Blueprint('main', __name__)
article_form = Blueprint('article_form', __name__)
publisher_form = Blueprint('publisher_form', __name__)

@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')

@main.route("/home-content")
def home_content():
    content = GetHomeContent() 
    return jsonify(content=content)

@article_form.route("/article")
def article():
    return render_template('article.html')

@article_form.route('/article-content')
def article_content():
    publishers = Publisher.query.all()
    nicks = []
    for pub in publishers:
        nicks.append(pub.nick)

    form = GetArticleContent()
    html_content = render_template_string(ArticleInput(nicks), form=form)
    return jsonify(content = html_content)

@article_form.route('/article-save', methods=['POST'])
def article_save():
    title = request.form['title']
    motto = request.form['motto']
    ilink = request.form['ilink']
    olink = request.form['olink']
    content = request.form['content']

    date_posted_str = request.form['date_posted']
    date_pub_str = request.form['date_pub']

    # Преобразуем строки в объекты datetime
    date_posted = datetime.strptime(date_posted_str, '%Y-%m-%d')
    date_pub = datetime.strptime(date_pub_str, '%Y-%m-%d')
    publisher_nick = request.form['publisher_nick']
    pub = Publisher.query.filter(Publisher.nick == publisher_nick).first()

    # преобразование основного текста
    content = transform(content)
    print(content)

    raise SystemExit  # ===================================================================

    with app.app_context():
#       создание новой статьи
        new_article = Articles(title=title, motto=motto, ilink=ilink, olink=olink, content=content,
                               date_posted=date_posted, date_pub=date_pub, publisher_id=pub.id)
        db.session.add(new_article)
        db.session.commit()

#       перенос изображений в папку images
        rename_and_move_files(new_article.id)

        return redirect(url_for('main.home'))

@publisher_form.route("/publisher")
def publisher():
    return render_template('publisher.html')

@publisher_form.route('/publisher-content')
def publisher_content():
    form = GetPublisherContent()
    html_content = render_template_string(PublisherInput(), form=form)
    return jsonify(content=html_content)

@publisher_form.route('/publisher-save', methods=['POST'])
def publisher_save():
    pub_name = request.form['pub_name']
    nick = request.form['nick']
    pub_status = request.form['pub_status']
    reference = request.form['reference']
    emblem = request.form['emblem']

    with app.app_context():
#       добавление нового издателя
        new_publisher = Publisher(name=pub_name, nick=nick, pub_status=pub_status, reference=reference, emblem=emblem)
        db.session.add(new_publisher)
        db.session.commit()
        return redirect(url_for('main.home'))
