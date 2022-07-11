import requests as req
import asyncio
import aiohttp
import aiofiles
import json


# 西游记
async def download(url, gid, index, info):
    data = {
        'book_id': str(gid),
        'cid': f'{gid}|{info["cid"]}',
        'need_book': 1
    }
    data = json.dumps(data)
    url = url + data
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            content = await resp.json()
            async with aiofiles.open('novel/' + str(index + 1) + info['title'] + '.txt',
                                     mode='w',
                                     encoding='utf-8')as f:
                await f.write(content['data']['novel']['content'])
                print('已完成', info['title'])


async def main(gid):
    # 拿到章节信息
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={"book_id"' + ':"' + str(gid) + '"}'
    resp = req.get(url)
    resp.encoding = 'utf-8'
    # 得到章节名和章节cid，cid下载链接需要使用
    catalogue = resp.json()['data']['novel']['items']
    tasks = []
    cUrl = 'https://dushu.baidu.com/api/pc/getChapterContent?data='
    for index, Info in enumerate(catalogue):
        tasks.append(download(cUrl, gid, index, Info))
    await asyncio.wait(tasks)


if __name__ == '__main__':
    # asyncio.run(main(4306063500))
    # 解决 RuntimeError: Event loop is closed
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(4306063500))
