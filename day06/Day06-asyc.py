import asyncio


# 异步协程

async def f(url):
    # 爬取请求
    await asyncio.sleep(2)  # 网络请求
    print('hello', str(url))


async def main():
    urls = [
        'www.baidu.com',
        'www.bilibili.com'
    ]
    tasks = []
    for url in urls:
        t = f(url)
        tasks.append(t)

    await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
