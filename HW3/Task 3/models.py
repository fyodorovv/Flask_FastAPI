from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Grade(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(50), nullable=False)
    grade = db.Column(db.Integer, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey(
        'student.id'), nullable=False)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    group = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    grades = db.relationship('Grade', backref='student')

    def __repr__(self):
        return f'<Student {self.name} {self.last_name}>'
