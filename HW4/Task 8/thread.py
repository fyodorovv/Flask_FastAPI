import requests
import threading

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/']


def download_url(url):
    response = requests.get(url)
    file_name = 'threading_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
    with open(file_name, 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    threads = []
    for url in urls:
        t = threading.Thread(target=download_url, args=(url,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
