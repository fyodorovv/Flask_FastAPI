import multiprocessing
import requests

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/']


def download_url(url):
    response = requests.get(url)
    file_name = 'multiprocessing_' + url.replace('https://','').replace('.', '_').replace('/', '') + '.html'
    with open(file_name, 'wb') as f:
        f.write(response.content)


if __name__ == '__main__':
    processes = []

    for url in urls:
        process = multiprocessing.Process(target=download_url, args=(url,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()
