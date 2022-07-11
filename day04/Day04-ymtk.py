import requests as req
from bs4 import BeautifulSoup
import time

# 优美图库
url = 'https://www.umei.cc/bizhitupian/xiaoqingxinbizhi/'
url = 'https://www.umei.cc/meinvtupian/siwameinv/'

resp = req.get(url)
# 网页编码为utf-8
resp.encoding = 'utf-8'

source = resp.text
# 将主页面传给bs4
main_page = BeautifulSoup(source, 'html.parser')
# 寻找需要的特定的标签 find
# 包含需要图片链接的div
div = main_page.find("div", class_="swiper-wrapper after")
# 获取链接列表，方便提取出子页面链接
a_list = div.find_all("a")

# href保存的不是完整地址，需要拼接
# 可以在浏览器中进行比较，发现需要拼接哪些
son_head_url = "https://www.umei.cc/"

for i, a in enumerate(a_list):
    # get方法可以拿到属性值 href就是a标签的一个属性值
    # 得到子页面的链接
    son_url = son_head_url + a.get("href")
    resp = req.get(son_url)
    resp.encoding = 'utf-8'
    source = resp.text
    son_page = BeautifulSoup(source, 'html.parser')
    # 得到图片的下载地址
    img_url = son_page.find('section', class_='img-content') \
        .find('img') \
        .get('src')
    # 访问图片地址，返回的只要图片本身的资源，保存即可
    img = req.get(img_url)
    # content 得到的二进制数据，用.jpg保存到本地
    with open('./img/' + str(i) + '.jpg', mode='wb') as f:
        f.write(img.content)
    print('已下载', i)
    time.sleep(2)
