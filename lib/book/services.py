from lib.extension import db
from lib.library_ma import BookSchema
from lib.model import Books
from flask import request

book_schema = BookSchema
books_schema = BookSchema(many=True)

def add_book_service():
    data = request.json
    if data and ('name' in data) and ('page_count' in data) and ('author_id' in data) and ('category_id' in data):
        name = data['name']
        page_count = data['page_count']
        author_id = data['author_id']
        category_id = data['category_id']
        try:
            new_book = Books(name, page_count, author_id, category_id)
            db.session.add(new_book)
            db.session.commit()
            return "Add success!"
        except IndentationError:
            db.session.rollback()
            return "Can not add book!"
    else:
        return "Request error"

def get_book_by_id_service(id):
    book = Books.query.get(id)
    if book:
        