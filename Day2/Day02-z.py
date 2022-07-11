import requests

url = "https://www.sogou.com/web?query=周杰伦"
# 在此次请求如果不添加，user-agent会被拦截，此字段会标识本机为浏览器访问，信息是在浏览器中进行查找，添加进来的
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
}
resp = requests.get(url, headers=headers)

print("req", resp.text)
