from marshmallow import Schema, fields, validates, ValidationError, post_load
from models import get_book_by_title, Book, Author

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)

    @validates('title')
    def validate_title(self, title):
        if get_book_by_title(title) is not None:
            raise ValidationError(
                'Book with title "{title}" already exists, '
                'please use a different title.'.format(title=title)
            )

    @post_load
    def create_book(self, data):
        return Book(**data)

class AuthorSchema(Schema):
    author_id = fields.Int(dump_only=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    middle_name = fields.Str()

    @post_load
    def create_author(self, data):
        return Author(**data)