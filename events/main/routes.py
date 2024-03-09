from flask import render_template, Blueprint, jsonify, render_template_string, request, redirect, url_for
from ..content_generators.home_content import GetHomeContent
from ..content_generators.article_content import GetArticleContent
from ..content_generators.article_input import ArticleInput
from ..content_generators.publisher_content import GetPublisherContent
from ..content_generators.publisher_input import PublisherInput
from events import db, app

import sys
from pathlib import Path
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent.parent
sys.path.append(str(parent_dir))
from dbase.models import Articles
from dbase.models import Publisher


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
    form = GetArticleContent()
    html_content = render_template_string(ArticleInput(), form=form)
    return jsonify(content = html_content)

@article_form.route('/article-save', methods=['POST'])
def article_save():
    title = request.form['title']
    content = request.form['content']
    with app.app_context():
#       создание новой статьи
        new_article = Articles(title=title, content=content, user_id=1)
        db.session.add(new_article)
        db.session.commit()
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

    with app.app_context():
#       добавление нового издателя
        new_publisher = Publisher(name=pub_name, nick=nick, pub_status=pub_status)
        db.session.add(new_publisher)
        db.session.commit()
        return redirect(url_for('main.home'))
