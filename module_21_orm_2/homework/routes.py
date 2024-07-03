from flask import Flask, request, jsonify
from datetime import datetime
from model import Book, Author, Student, ReceivingBook, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db.init_app(app)

# Routes
@app.route('/books_by_author/<int:author_id>', methods=['GET'])
def get_books_by_author(author_id):
    books = Book.query.filter_by(author_id=author_id).all()
    return jsonify([book.name for book in books])

@app.route('/unseen_books/<int:student_id>', methods=['GET'])
def get_unseen_books(student_id):
    books = Book.query.filter(Book.author_id.in_(
        db.session.query(Book.author_id).join(ReceivingBook, ReceivingBook.book_id == Book.id)
        .filter(ReceivingBook.student_id == student_id))).all()
    return jsonify([book.name for book in books])

@app.route('/average_books_per_student_in_month', methods=['GET'])
def get_average_books_per_student_in_month():
    # Implementation depends on data organization for book issuance to students
    pass

@app.route('/most_popular_book_above_score_4', methods=['GET'])
def get_most_popular_book_above_score_4():
    # Implementation depends on data organization for books read by students
    pass

@app.route('/top_10_readers_in_year', methods=['GET'])
def get_top_10_readers_in_year():
    # Implementation depends on data organization for book issuance to students
    pass

# Handling CSV file
from csv import DictReader

@app.route('/insert_students_from_csv', methods=['POST'])
def insert_students_from_csv():
    file = request.files['file']
    if file.filename.endswith('.csv'):
        csv_reader = DictReader(file, delimiter=';')
        students = []
        for row in csv_reader:
            student = {
                'name': row['name'],
                'surname': row['surname'],
                'phone': row['phone'],
                'email': row['email'],
                'average_score': float(row['average_score']),
                'scholarship': bool(row['scholarship'])
            }
            students.append(student)
        with db.session.begin_nested():
            # Add logic to insert students into database
            pass
    return "Students inserted successfully"

if __name__ == '__main__':
    app.run(debug=True)