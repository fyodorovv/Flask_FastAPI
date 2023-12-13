from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    context = [
        {'title': 'Новость 1', 'news_content': 'Описание новости 1',
            'date': '2023-12-11'},
        {'title': 'Новость 2', 'news_content': 'Описание новости 2',
            'date': '2023-12-12'},
        {'title': 'Новость 3', 'news_content': 'Описание новости 3',
            'date': '2023-12-13'},
    ]
    return render_template('index.html', context=context)


if __name__ == "__main__":
    app.run(debug=True)
