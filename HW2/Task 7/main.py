from flask import Flask, request, render_template, redirect, url_for


app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('form'))


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        num = request.form.get('num')
        return f'Квадрат числа равен {int(num) ** 2}!'
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
