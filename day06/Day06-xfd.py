import requests as req
import csv
import time
from concurrent.futures import ThreadPoolExecutor

# 北京新发地


# 写入csv文件中
f = open('xfd.csv', mode='w', encoding='utf-8', newline='')
cf = csv.writer(f)


def download(current):
    # 相关变化参数，设置在函数内部，不然会被线程公用同一时间读取的参数一致时，导致下载数据重复
    url = 'http://www.xinfadi.com.cn/getPriceData.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49'
    }
    params = {
        'limit': 20,
        'current': current,
        'pubDateStartTime': '',
        'pubDateEndTime': '',
        'prodPcatid': '',
        'prodCatid': '',
        'prodName': ''
    }
    resp = req.get(url, headers=headers, params=params)
    resp.encoding = 'utf-8'
    one_page = resp.json()['list']
    for one in one_page:
        cf.writerow(one.values())
    print("已完成", params['current'])
    time.sleep(1)


if __name__ == '__main__':
    # for i in range(2):
    #     params['current'] = i+1
    #     download(url, headers, params)
    # 线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            # 页码从1开始
            current = i + 1
            args = [current]
            t.submit(lambda p: download(*p), args)
