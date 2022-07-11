import requests as req
import re
import csv
import time

url = "https://movie.douban.com/top250"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
}


def get_t250(start):
    params = {  # 不同的页面，循环爬取
        'start': start
    }
    resp = req.get(url, headers=headers, params=params)

    obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<movieName>.*?)'
                     r'</span>.*?<p class="">.*?<br>(?P<movieYear>.*?)&nbsp.*?'
                     r'<span class="rating_num" property="v:average">(?P<movieRate>.*?)'
                     r'</span>.*?<span>(?P<people>.*?)人评价</span>',
                     re.S)

    result = obj.finditer(resp.content.decode('utf-8'))

    # for it in result:
    #     print(it.group("movieName"))
    #     print(it.group("movieYear").strip())
    #     print(it.group("movieRate"))
    #     print(it.group("people"))

    # 保存到csv中 newline=''写入一行后取消自动换行，不然没写入一条会多出一行空白
    f = open("t250.csv", mode='a', encoding='utf-8', newline='')
    cf = csv.writer(f)
    for it in result:
        ditc = it.groupdict()
        ditc['movieYear'] = ditc['movieYear'].strip()
        # print(ditc.values())
        cf.writerow(ditc.values())
    f.close()

    print("已写入", start)
    # 睡眠三秒
    time.sleep(3)


if __name__ == '__main__':
    for start in range(0, 10):
        get_t250(start * 25)
