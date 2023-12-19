from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from form import RegisterForm
from models import db, User

app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///4.sqlite'
db.init_app(app)
csrf = CSRFProtect(app)


def add_user(username, email, password):
    user = User(username=username, email=email, password=password)
    db.session.add(user)
    db.session.commit()
    print('Пользователь добавлен!')


@app.route('/', methods=['GET', 'POST'])
def register():
    notifications = []
    form = RegisterForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        if User.query.filter(User.username == username).count() > 0:
            notifications.append(f'Имя {username} занято!')
        if User.query.filter(User.email == email).count() > 0:
            notifications.append(f'Email {email} занято!')
        else:
            password = form.password.data
            add_user(username, email, password)
            notifications.append(f'Пользователь {username} добавлен!')
            render_template('register.html', form=form,
                            notifications=notifications)

    return render_template('register.html', form=form, notifications=notifications)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK!')
