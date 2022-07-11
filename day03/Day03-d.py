import requests as req

# 抓取豆瓣分类中的电影，如科幻分类

url = "https://movie.douban.com/j/new_search_subjects"
# get请求参数的另一种写法，在调用req.get方法时传入，自动拼接
params = {
    'sort': "T",
    'range': [0, 10],
    'tags': '',
    'start': '0',
    'genres': '科幻'
}
# 请求头，处理反爬的首选，先添加user-agent
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
}
resp = req.get(url, params=params, headers=headers)
print(resp.json())

with open("douBan.json", mode='w') as f:
    f.write(str(resp.json()))
