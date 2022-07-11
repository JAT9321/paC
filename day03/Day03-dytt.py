import requests as req
import re

# 盗版天堂
url = 'https://dy.dytt8.net/index2.htm'
resp = req.get(url, verify=False)  # verify=False 取消安全验证
# 查看网页中的charset为gb2312
web = resp.content.decode("gb2312")
obj = re.compile(r'.*?2022新片精品.*?<ul>(?P<movie>.*?)</ul>',
                 re.S)
# 分出2022新片中的每个影片的链接地址
obj2 = re.compile(r"<a href='(?P<mto>.*?)'",
                  re.S)
# 跳转到每个电影页面时，获取下载链接及其片名
obj3 = re.compile(r'译　　名　(?P<name>.*?)<br />'
                  r'.*?下载地址2：<a href="(?P<down_url>.*?)"',
                  re.S)

# 将2022新片整体切出
result = obj.finditer(web)
# 保存完整的影片url
hrefs = []
# url_global = https://dy.dytt8.net
url_global = url.replace('/index2.htm', '')

# 这里的外循环只会进行一次，因为切割的是具体的2022新片
for it in result:
    movie2022 = it.group("movie")
    result2 = obj2.finditer(movie2022)
    for it2 in result2:
        mto = it2.group('mto')
        mto = url_global + mto
        hrefs.append(mto)
# 2022年7月6日 第一个不是电影链接，移除
hrefs.pop(0)
for href in hrefs:
    # print(href)
    resp = req.get(href, verify=False)
    resp.encoding = 'gb2312'
    web = resp.text
    result = obj3.finditer(web)
    for it in result:
        print(it.group("name"))
        print(it.group("down_url"))
