from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('form'))


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        try:
            age = int(age)
        except ValueError:
            return "Возраст должен быть числом!"
        if age < 18:
            return "Вам нет 18!"
        return f'Привет {age}-х летний {name}!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
