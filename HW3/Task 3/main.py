from random import choice, randint
from flask import Flask, render_template
from models import db, Student, Grade
from faker import Faker

fake = Faker("ru_RU")

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///3.sqlite'
db.init_app(app)


@app.route('/')
def index():
    students = Student.query.all()
    context = {'students': students}
    return render_template('grade.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK!')


@app.cli.command('fill-db')
def fill_db():
    subjects = [f'Предмет{i}' for i in range(1, 5)]
    groups = [f"Группа{i}" for i in range(1, 3)]
    for _ in range(10):
        student = Student(
            name=fake.first_name(),
            last_name=fake.last_name(),
            group=choice(groups),
            email=fake.safe_email(),
        )
        db.session.add(student)
        print(f'Студент добавлен: {student}')

        for _ in range(20):
            grade = Grade(
                subject=choice(subjects),
                grade=randint(2, 5),
                student=student,
            )
            db.session.add(grade)

        print(f'Оценки добавлены: {student}')

    db.session.commit()
    print('База данных заполнена данными!')


if __name__ == '__main__':
    app.run(debug=True)
