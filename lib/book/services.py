from lib.extension import db
from lib.library_ma import BookSchema
from lib.model import Books
from flask import request

book_schema = BookSchema
books_schema = BookSchema(many=True)

def add_book_service():
    name = request.json['name']
    page_count = request.json['page_count']
    author_id = request.json['author_id']
    category_id = request.json['category_id']
    try:
        new_book = Books(name, page_count, author_id, category_id)
        db.session.add(new_book)
        db.session.commit()
        return "Add success!"
    except IndentationError:
        db.session.rollback()
        return "Can not add book!"