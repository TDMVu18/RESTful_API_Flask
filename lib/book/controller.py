from flask import Blueprint
from .services import add_book_service

books = Blueprint("books", __name__)
@books.route("/get-all-book")
def get_all_book():
    return "All book"


@books.route("/book-management/book", methods = ['POST'])
def add_book():
    return add_book_service()