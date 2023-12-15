from flask import Flask, render_template, request, make_response, redirect, url_for


app = Flask(__name__)
app.secret_key = b'5f214cacbd30c2ae4784b520f17912ae0d5d8c16ae98128e3f549546221265e4'


@app.route('/')
def index():
    return redirect(url_for('cookie_form'))


@app.route('/cookie_form', methods=['GET', 'POST'])
def cookie_form():
    if request.method == 'POST':
        response = make_response(redirect(url_for('del_cookie')))
        response.set_cookie('name', request.form.get('name'))
        response.set_cookie('email', request.form.get('email'))
        return response
    return render_template('cookie.html')


@app.route('/del_cookie', methods=['GET', 'POST'])
def del_cookie():
    if request.method == 'POST':
        response = make_response(redirect(url_for('cookie_form')))
        response.delete_cookie('name')
        response.delete_cookie('email')
        return response
    name = request.cookies.get('name')
    return render_template('del_cookie.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
