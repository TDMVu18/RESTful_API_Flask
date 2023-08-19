from flask import Flask, request, Blueprint
from .book.controller import books
from .extension import db, ma
import os
from .model import Students, Books, Borrows, Author, Category


def create_app(config_file="config.py"):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///lib.db"
    db.init_app(app)
    ma.init_app(app)
    app.config.from_pyfile(config_file)

    with app.app_context():
        db.create_all()
        print("created")
    app.register_blueprint(books)

    return app