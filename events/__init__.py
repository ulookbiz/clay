from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
app = Flask(__name__)

def create_app():

    app.config['SECRET_KEY'] = 'Kjdyte_=pvugebkd'

    basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    database_path = os.path.join(basedir, 'dbase', 'instance', 'site.db').replace('\\', '/')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_path
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    from events.main.routes import main,article_form,publisher_form

    app.register_blueprint(main)
    app.register_blueprint(article_form)
    app.register_blueprint(publisher_form)

    return app
