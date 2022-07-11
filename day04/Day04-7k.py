import requests as req

# 17k小说
url = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'

headers = {
    'Accept': '*/*',
    'Cookie': 'GUID=609c1c07-ed71-4ba6-858c-9de4c1b07a2b; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F08%252F28%252F45%252F97254528.jpg-88x88%253Fv%253D1657197644000%26id%3D97254528%26nickname%3D%25E4%25B9%25A6%25E5%258F%258BeC7wcqJb4%26e%3D1672749993%26s%3D8c82b9b4468bbcb4; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2297254528%22%2C%22%24device_id%22%3A%22181d8a144baddc-0990c93200813e-4a617f5c-1328640-181d8a144bb1563%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fgraph.qq.com%2F%22%2C%22%24latest_referrer_host%22%3A%22graph.qq.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%22609c1c07-ed71-4ba6-858c-9de4c1b07a2b%22%7D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44'
}

resp = req.get(url, headers=headers)
resp.encoding = 'utf-8'
print(resp.json())
