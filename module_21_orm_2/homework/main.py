from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey, exc

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)

# Таблица книг в библиотеке
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    count = db.Column(db.Integer, default=1)
    release_date = db.Column(db.Date, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

# Таблица авторов
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    books = relationship("Book", backref="author")

# Таблица читателей
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    average_score = db.Column(db.Float, nullable=False)
    scholarship = db.Column(db.Boolean, nullable=False)
    receiving_books = relationship("ReceivingBook", backref="student")

# Таблица выдачи книг студентам
class ReceivingBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'))
    date_of_issue = db.Column(db.DateTime, nullable=False)
    date_of_return = db.Column(db.DateTime)
    count_date_with_book = db.Column(db.Integer)

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return is not None:
            return (self.date_of_return - self.date_of_issue).days
        else:
            return (datetime.now() - self.date_of_issue).days

db.create_all()

# роуты
@app.route('/books_by_author/<int:author_id>', methods=['get'])
def get_books_by_author(author_id):
    books = Book.query.filter_by(author_id=author_id).all()
    return jsonify([book.name for book in books])

@app.route('/unseen_books/<int:student_id>', methods=['get'])
def get_unseen_books(student_id):
    books = Book.query.filter(Book.author_id.in_(db.session.query(Book.author_id).join(ReceivingBook, ReceivingBook.book_id == Book.id).filter(ReceivingBook.student_id == student_id))).all()
    return jsonify([book.name for book in books])

@app.route('/average_books_per_student_in_month', methods=['get'])
def get_average_books_per_student_in_month():
    # Реализация этого метода зависит от того, как у вас организованы данные по выдаче книг студентам
    pass

@app.route('/most_popular_book_above_score_4', methods=['get'])
def get_most_popular_book_above_score_4():
    students = Student.query.filter(Student.average_score > 4.0).all()
    # Реализация этого метода зависит от того, как у вас организованы данные по читаемым книгам студентов
    pass

@app.route('/top_10_readers_in_year', methods=['get'])
def get_top_10_readers_in_year():
    # Реализация этого метода зависит от того, как у вас организованы данные по выдаче книг студентам
    pass

# Обработка CSV-файла

from csv import DictReader

@app.route('/add_students', methods=['post'])
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