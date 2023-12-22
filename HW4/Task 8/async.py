import aiohttp
import asyncio

urls = ['https://www.google.ru/',
        'https://gb.ru/',
        'https://ya.ru/',
        'https://www.python.org/',
        'https://habr.com/ru/all/']


async def download_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            file_name = 'asyncio_' + url.replace('https://', '').replace('.', '_').replace('/', '') + '.html'
            with open(file_name, 'wb') as f:
                f.write(await resp.read())


async def main():
    tasks = []
    for url in urls:
        tasks.append(download_url(url))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())
