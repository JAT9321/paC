import requests as req

# post 请求
url = "https://fanyi.baidu.com/sug"

body_json = {
    'kw': '狗'
}
resp = req.post(url, data=body_json)
print(resp.json())
