from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.hybrid import hybrid_property

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///library.db'
db = SQLAlchemy(app)

# таблица книг в библиотеке
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    count = db.Column(db.Integer, default=1)
    release_date = db.Column(db.Date, nullable=False)
    author_id = db.Column(db.Integer, nullable=False)

# таблица авторов
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)

# таблица читателей
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    average_score = db.Column(db.Float, nullable=False)
    scholarship = db.Column(db.Boolean, nullable=False)

# таблица выдачи книг студентам
class ReceivingBook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, nullable=False)
    date_of_issue = db.Column(db.DateTime, nullable=False)
    date_of_return = db.Column(db.DateTime)

    @hybrid_property
    def count_date_with_book(self):
        if self.date_of_return is not None:
            return (self.date_of_return - self.date_of_issue).days
        else:
            return (datetime.now() - self.date_of_issue).days

    @classmethod
    def get_students_with_scholarship(cls):
        return Student.query.filter_by(scholarship=True).all()

    @classmethod
    def get_students_with_score_above(cls, score):
        return Student.query.filter(Student.average_score > score).all()

# Роуты
@app.route('/books', methods=['GET'])
def get_all_books():
    books = Book.query.all()
    return jsonify([book.name for book in books])

@app.route('/debtors', methods=['GET'])
def get_debtors():
    debtors = ReceivingBook.query.filter(ReceivingBook.count_date_with_book > 14).all()
    return jsonify([debtor.student_id for debtor in debtors])

@app.route('/issue-book', methods=['POST'])
def issue_book():
    data = request.json
    new_receiving = ReceivingBook(book_id=data['book_id'], student_id=data['student_id'], date_of_issue=datetime.now())
    db.session.add(new_receiving)
    db.session.commit()
    return jsonify({'message': 'Book issued successfully'})

@app.route('/return-book', methods=['POST'])
def return_book():
    data = request.json
    receiving = ReceivingBook.query.filter_by(book_id=data['book_id'], student_id=data['student_id']).first()
    if receiving is not None:
        receiving.date_of_return = datetime.now()
        db.session.commit()
        return jsonify({'message': 'Book returned successfully'})
    else:
        return jsonify({'error': 'No such book-student pair found'})

if __name__ == '__main__':
    app.run(debug=True)