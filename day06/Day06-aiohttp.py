import aiohttp
import asyncio

urls = [
    # 自己的毕设网站
    'http://106.14.219.106:20918/images/69da60b7-1afa-4fe8-8ad8-d1fda3b439ef.jpg',
    'http://106.14.219.106:20918/images/ad2b3eb7-14b6-40b6-8caa-3766acba189d.jpg'
]


async def download(url):
    name = url.rsplit(r'/', 1)[1]
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open('images/' + str(name), mode='wb') as f:
                f.write(await resp.content.read())  # 此处的resp.content.read()与之前的resp.content()一样


async def main():
    tasks = []
    for url in urls:
        tasks.append(download(url))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
