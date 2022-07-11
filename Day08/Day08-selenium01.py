from selenium.webdriver import Edge

# 创建浏览器对象
web = Edge()

web.get('http://www.bilibili.com')

print(web.title)
