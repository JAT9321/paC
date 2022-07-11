import requests as req
import re
import time
import asyncio
import aiofiles
import aiohttp
import os

url = 'https://play.xn--55q3u83bh7en9loko5ta801klezbe5aw98bnjblz1e.com/index.php?url=https://cdn7.caoliqi.com:65/20220708/3pwt0JO3/index.m3u8'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49"
}

resp = req.get(url, headers=headers)
resp.encoding = 'utf-8'

obj = re.compile(r"url: '(?P<m3u8_url>.*?)',"
                 , re.S)
result = obj.search(resp.text)
m3u8_url = result.group('m3u8_url')
resp.close()
print('url', result['m3u8_url'])

resp = req.get(m3u8_url, headers=headers, verify=False)

with open('really.m3u8', mode='wb') as f:
    f.write(resp.content)
with open('really.m3u8', mode='r') as f:
    content = f.readlines()
    m3u8_url = url.split('=')[1] \
                   .rsplit('/', 3)[0] \
               + str(content[2])
resp.close()
print('m3u8_url', m3u8_url.strip())

resp = req.get(m3u8_url.strip(), headers=headers, verify=False)
# print(resp.content)
with open('xc.m3u8', mode='wb') as f:
    f.write(resp.content)
resp.close()

pre_url = url.split('=')[1].rsplit('/', 3)[0]


# 协程
async def get_name(name):
    if name < 10:
        return '00' + str(name) + '.ts'
    if name < 100:
        return '0' + str(name) + '.ts'
    return str(name) + '.ts'


async def download(session, url, name):
    async with session.get(url) as resp:
        name = await get_name(name)
        async with aiofiles.open('video/xc/' + name, mode='wb') as f:
            ts = await resp.content.read()
            await f.write(ts)
            print('已完成', name)


async def main():
    tasks = []
    index = 0
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open('xc.m3u8', mode='r') as f:
            async for line in f:
                line = line.strip()
                # 不需要井号开头的
                if (line.startswith("#")):
                    continue
                # 完整.ts的url
                down_url = pre_url + line
                # name = str(line).rsplit('/', 1)[1]
                index = index + 1
                name = index
                task = asyncio.create_task(download(session, down_url, name))
                tasks.append(task)
            await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(main())
    # 解决 RuntimeError: Event loop is closed
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
