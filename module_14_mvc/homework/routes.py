from flask import Flask, render_template, request, redirect
from typing import List
from werkzeug import Response
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField
from wtforms.validators import InputRequired
from models import init_db, get_all_books, DATA, add_new_book, get_all_abouts
from module_04_flask.materials.get_requests import search

app: Flask = Flask(__name__)


class AddBookForm(FlaskForm):
    title = StringField(validators=[InputRequired()])
    author = StringField(validators=[InputRequired()])


class SearchForm(FlaskForm):
    author = StringField(validators=[InputRequired()])


def _get_html_table_for_books(books: List[dict]) -> str:
    table = """
<table>
    <thead>
    <tr>
        <th>ID</td>
        <th>Title</td>
        <th>Author</td>
    </tr>
    </thead>
    <tbody>
        {books_rows}
    </tbody>
</table>
"""
    rows: str = ''
    for book in books:
        rows += '<tr><td>{id}</tb><td>{title}</tb><td>{author}</tb></tr>'.format(
            id=book['id'], title=book['title'], author=book['author'],
        )
    return table.format(books_rows=rows)


@app.route('/books')
def all_books() -> str:
    abouts = get_all_abouts()
    return render_template(
        'index.html',
        books=get_all_books(), abouts=abouts
    )


@app.route('/books/form', methods=['post', 'get'])
def get_books_form() -> Response | str:
    form = AddBookForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            data = form.title.data, form.author.data
            add_new_book(data)
        return redirect('/books')
    else:
        return render_template('add_book.html', form=form)


@app.route('/books/author', methods=['post', 'get'])
def search_by_author():
    form = SearchForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            author = form.author.data
            return render_template('find_book.html', books=search(author),)
    else:
        return render_template('author.html', form=form)


@app.route('/books/<int:id_book>')
def get_about(id_book: int):
    return render_template('about.html', book=about(id_book))

if __name__ == '__main__':
    app.config["WTF_CSRF_ENABLED"] = False
    init_db(DATA)
    app.run(debug=True)
