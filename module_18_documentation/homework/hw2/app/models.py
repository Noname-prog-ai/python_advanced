import sqlite3
from dataclasses import dataclass
from typing import Optional, Union, List, Dict

enable_foreign_key = "PRAGMA foreign_keys = ON;"

data_books = [
    {'id': 1, 'title': 'a byte of python', 'author': 1},
    {'id': 2, 'title': 'moby-dick; or, the whale', 'author': 2},
    {'id': 3, 'title': 'war and peace', 'author': 3},
]

data_authors = [
    {'author_id': 1, 'first_name': 'станислав', 'last_name': 'лем', 'middle_name': 'герман'},
    {'author_id': 2, 'first_name': 'herman', 'last_name': 'melville', 'middle_name': '_'},
    {'author_id': 3, 'first_name': 'leo', 'last_name': 'tolstoy', 'middle_name': 'николаевич'},
]

database_name = 'table_books.db'
books_table_name = 'books'
author_table_name = 'authors'


@dataclass
class Book:
    title: str
    author: str
    id: Optional[int] = None

    def __getitem__(self, item: str) -> Union[int, str]:
        return getattr(self, item)


@dataclass
class Author:
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    author_id: Optional[int] = None

    def __getitem__(self, item):
        return getattr(self, item)


def init_db(initial_records_authors: List[Dict], initial_records_books: List[Dict]) -> None:
    with sqlite3.connect(database_name) as conn:
        conn.execute(enable_foreign_key)
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT name FROM sqlite_master
            WHERE type='table' AND name='{author_table_name}';
            """
        )
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(
                f"""
                CREATE TABLE IF NOT EXISTS authors (
                author_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(50) NOT NULL,
                middle_name VARCHAR(50)
                )
                """
            )
            cursor.executemany(
                f"""
                    INSERT INTO {author_table_name}
                    (first_name, last_name, middle_name) VALUES (?, ?, ?)
                """,
                [(item['first_name'], item['last_name'], item['middle_name']) for item in initial_records_authors]
            )

            cursor.execute(
                f"""
                SELECT name FROM sqlite_master
                WHERE type='table' AND name='{books_table_name}';
                """
            )
            exists = cursor.fetchone()
            if not exists:
                cursor.executescript(
                    f"""
                    CREATE TABLE {books_table_name}(
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        title TEXT,
                        author INTEGER NOT NULL REFERENCES authors(author_id) ON DELETE CASCADE
                    )
                    """
                )
                cursor.executemany(
                    f"""
                    INSERT INTO {books_table_name}
                    (title, author) VALUES (?, ?)
                    """,
                    [(item['title'], item['author']) for item in initial_records_books]
                )


def _get_book_obj_from_row(row: tuple) -> Book:
    return Book(id=row[0], title=row[1], author=row[2])


def _get_author_obj_from_row(row: tuple) -> Author:
    return Author(author_id=row[0], first_name=row[1], last_name=row[2], middle_name=row[3])


def get_all_books() -> List[Book]:
    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {books_table_name}')
        all_books = cursor.fetchall()
        return [_get_book_obj_from_row(row) for row in all_books]


def get_all_authors() -> List[Author]:
    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()
        cursor.execute(f'SELECT * FROM {author_table_name}')
        all_authors = cursor.fetchall()
        return [_get_author_obj_from_row(row) for row in all_authors]


def add_book(new_book: Book) -> Book:
    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            INSERT INTO {books_table_name} 
            (title, author) VALUES (?, ?)
            """,
            (new_book.title, new_book.author)
        )
        new_book.id = cursor.lastrowid
        return new_book


def get_book_by_id(book_id: int) -> Optional[Book]:
    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            SELECT * FROM {books_table_name} WHERE id = ?
            """,
            (book_id,)
        )
        book = cursor.fetchone()
        if book:
            return _get_book_obj_from_row(book)


def update_book_by_id(updated_book: Book) -> None:
    with sqlite3.connect(database_name) as conn:
        cursor = conn.cursor()
        cursor.execute(
            f"""
            UPDATE {books_table_name} SET title = ?, author = ?
            WHERE id = ?
            """,
            (updated_book.title, updated_book.author, updated_book.id)
        )