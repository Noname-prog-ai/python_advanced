from flask import Flask, request
from flask_restx import Api, Resource
from marshmallow import ValidationError

from models import (
    data_books,
    data_authors,
    get_all_books,
    get_all_authors,
    init_db,
    add_book,
    add_author,
    get_book_by_id,
    update_book_by_id,
    delete_book_by_id,
    get_book_by_author,
)
from schemas import BookSchema, AuthorSchema

app = Flask(__name__)
api = Api(app)

class BookList(Resource):
    def get(self):
        schema = BookSchema()
        return schema.dump(get_all_books(), many=True), 200

    def post(self):
        data = request.json
        schema = BookSchema()
        try:
            book = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        book = add_book(book)
        return schema.dump(book), 201

class AuthorsList(Resource):
    def get(self):
        schema = AuthorSchema()
        return schema.dump(get_all_authors(), many=True), 200

    def post(self):
        data = request.json
        schema = AuthorSchema()
        try:
            author = schema.load(data)
        except ValidationError as exc:
            return exc.messages, 400

        author = add_author(author)
        return schema.dump(author), 200

class Authors(Resource):
    def delete(self, author_id):
        return delete_book_by_id(author_id), 200

    def get(self, author_id):
        schema = BookSchema()
        return schema.dump(get_book_by_author(author_id), many=True), 200

class BooksEdit(Resource):
    def get(self, book_id):
        schema = BookSchema()
        return schema.dump(get_book_by_id(book_id)), 200

    def put(self, book_id):
        data = request.json
        book = {'title': data['title'], 'author': data['author']}
        return update_book_by_id(book_id, book), 200

    def patch(self, book_id):
        data = request.json
        book_for_edit = get_book_by_id(book_id)
        for key, value in data.items():
            setattr(book_for_edit, key, value)
        update_book_by_id(book_for_edit)
        return 200

    def delete(self, book_id):
        return delete_book_by_id(book_id), 200

api.add_resource(BookList, '/api/books', '/api/books/<int:book_id>')
api.add_resource(AuthorsList, '/api/authors')
api.add_resource(Authors, '/api/authors/<int:author_id>')
api.add_resource(BooksEdit, '/api/books/<int:book_id>')

if __name__ == '__main__':
    init_db(initial_records_books=data_books, initial_records_authors=data_authors)
    app.run(debug=True)