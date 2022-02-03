from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import settings

database = SQLAlchemy()
marshmallow = Marshmallow()


def register_database(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI

    database.init_app(app)
    marshmallow.init_app(app)

    return app


def create_all_table(app):
    with app.app_context():
        try:
            from repository.orm import Idea
            database.create_all()
        except Exception as e:
            print("database already exists: " + str(e))

