from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, DateTime
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import create_engine, event, exc
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)

# отдельные таблицы для каждой модели

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    count = Column(Integer, default=1)
    release_date = Column(Date, nullable=False)
    author_id = Column(Integer, ForeignKey('authors.id'))

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    books = relationship("Book", backref="author")

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    phone = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    average_score = Column(Float, nullable=False)
    scholarship = Column(Boolean, nullable=False)
    receiving_books = relationship("ReceivingBook", backref="student")

class ReceivingBook(Base):
    __tablename__ = 'receiving_books'
    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey('books.id'))
    student_id = Column(Integer, ForeignKey('students.id'))
    date_of_issue = Column(DateTime, nullable=False)
    date_of_return = Column(DateTime)

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return is not None:
            return (self.date_of_return - self.date_of_issue).days
        else:
            return (datetime.now() - self.date_of_issue).days

Base.metadata.create_all(db.engine)

# отдельные роуты для каждого метода


@app.route('/books_by_author/<int:author_id>', methods=['GET'])
def get_books_by_author(author_id):
    books = Book.query.filter_by(author_id=author_id).all()
    return jsonify([book.name for book in books])

@app.route('/unseen_books/<int:student_id>', methods=['GET'])
def get_unseen_books(student_id):
    books = Book.query.filter(Book.author_id.in_(db.session.query(Book.author_id).join(ReceivingBook, ReceivingBook.book_id == Book.id).filter(ReceivingBook.student_id == student_id))).all()
    return jsonify([book.name for book in books])

@app.route('/average_books_per_student_in_month', methods=['GET'])
def get_average_books_per_student_in_month():
    # реализация этого метода зависит от того, как у вас организованы данные по выдаче книг студентам
    pass

@app.route('/most_popular_book_above_score_4', methods=['GET'])
def get_most_popular_book_above_score_4():
    students = Student.query.filter(Student.average_score > 4.0).all()
    # реализация этого метода зависит от того, как у вас организованы данные по читаемым книгам студентов
    pass

@app.route('/top_10_readers_in_year', methods=['GET'])
def get_top_10_readers_in_year():
    # реализация этого метода зависит от того, как у вас организованы данные по выдаче книг студентам
    pass

# обработка csv-файла

from csv import DictReader

@app.route('/add_students', methods=['POST'])
def add_students():
    file = request.files['file']
    if file:
        students = DictReader(file, delimiter=';')
        bulk_data = []
        for student in students:
            bulk_data.append({
                'name': student['name'],
                'surname': student['surname'],
                'phone': student['phone'],
                'email': student['email'],
                'average_score': float(student['average_score']),
                'scholarship': True if student['scholarship'] == 'True' else False
            })

        try:
            db.session.bulk_insert_mappings(Student, bulk_data)
            db.session.commit()
            return jsonify({'message': 'Students added successfully'})
        except exc.IntegrityError:
            db.session.rollback()
            return jsonify({'error': 'Phone number format is incorrect'})

if __name__ == '__main__':
    app.run(debug=True)