"""
Заменим сообщение "The requested URL was not found on the server" на что-то более информативное.
Например, выведем список всех доступных страниц с возможностью перехода по ним.

Создайте Flask Error Handler, который при отсутствии запрашиваемой страницы будет выводить
список всех доступных страниц на сайте с возможностью перехода на них.
"""

from flask import Flask, render_template_string, abort

app = Flask(__name__)

# Список всех доступных страниц с возможностью перехода
page_links = [
    ('/dogs', 'Страница с пёсиками'),
    ('/cats', 'Страница с котиками'),
    ('/cats/<int:cat_id>', 'Страница с котиком {cat_id}'),
    ('/index', 'Главная страница')
]

# Обработчик ошибки 404
@app.errorhandler(404)
def page_not_found(error):
    return render_template_string(
        '<h1>Страница не найдена</h1>'
        '<p>Список всех доступных страниц:</p>'
        '<ul>{% for link, name in page_links %}'
        '<li><a href="{{ link }}">{{ name }}</a></li>{% endfor %}</ul>'
    , page_links=page_links), 404

@app.route('/dogs')
def dogs():
    return 'Страница с пёсиками'


@app.route('/cats')
def cats():
    return 'Страница с котиками'


@app.route('/cats/<int:cat_id>')
def cat_page(cat_id: int):
    return f'Страница с котиком {cat_id}'


@app.route('/index')
def index():
    return 'Главная страница'


if __name__ == '__main__':
    app.run(debug=True)
