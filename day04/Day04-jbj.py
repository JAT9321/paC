import requests as req
from lxml import etree

# 猪八戒
url = 'https://task.zbj.com/hall/list/h1'
resp = req.get(url)
resp.encoding = 'utf-8'
# print(resp.text)
# 解析
html = etree.HTML(resp.text)
result = html.xpath('/html/body/div[1]/div[6]/div/div[2]/div[2]/div/div[1]/div')
for r in result:
    print('名称', r.xpath('./div[1]/h4/a/text()')[0])
    print('地址', r.xpath('./div[3]/span[4]/text()')[0])
    # print(r.xpath('./div[4]/span/@class')[0])# @class 是获取标签里的属性值，@href等
    print('价格', str(r.xpath('./div[4]/span/text()')[0]).split('￥')[1])
