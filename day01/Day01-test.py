import urllib.request as req

url = "http://www.baidu.com"

# urlopen 进行url跳转，并获得页面源代码
resp = req.urlopen(url)
# 按照爬出的网页编码格式，进行解码，一般在网页头中可以看到编码格式。
print(resp.read().decode("utf-8"))

# 将爬出的页面保存成文件，可以点击进行访问
with open("test01.html", mode='w', encoding='utf-8') as f:
    f.write(resp.read().decode("utf-8"))
