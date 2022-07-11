import requests as req
import re
import time

url = 'https://play.xn--55q3u83bh7en9loko5ta801klezbe5aw98bnjblz1e.com/index.php?url=https://cdn7.caoliqi.com:65/20220708/3pwt0JO3/index.m3u8'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49"
}

resp = req.get(url, headers=headers)
resp.encoding = 'utf-8'
# 需要的链接在script里，使用re正则
# 注意源码中url两侧的单引号，cao
obj = re.compile(r"url: '(?P<m3u8_url>.*?)',"
                 , re.S)
result = obj.search(resp.text)
m3u8_url = result.group('m3u8_url')
resp.close()
print('url', result['m3u8_url'])

resp = req.get(m3u8_url, headers=headers, verify=False)

# 写入存放m3u8真正地址的文件
with open('really.m3u8', mode='wb') as f:
    f.write(resp.content)
with open('really.m3u8', mode='r') as f:
    # 得到真正m3u8的地址，和之前不同了
    content = f.readlines()
    # print(content[2]) 地址 /20220708/3pwt0JO3/1215kb/hls/index.m3u8
    # 得到真正的m3u8完整地址
    # split 得到https://cdn7.caoliqi.com:65/20220708/3pwt0JO3/index.m3u8
    # rsplit 得到https://cdn7.caoliqi.com:65
    # +str 得到https://cdn7.caoliqi.com:65/20220708/3pwt0JO3/1215kb/hls/index.m3u8
    m3u8_url = url.split('=')[1] \
                   .rsplit('/', 3)[0] \
               + str(content[2])
resp.close()
print('m3u8_url', m3u8_url.strip())
# 得到影片真正完整的m3u8
# 记得去除多余空格，我是中招了，做了也不费劲
resp = req.get(m3u8_url.strip(), headers=headers, verify=False)
# print(resp.content)
with open('easy.m3u8', mode='wb') as f:
    f.write(resp.content)
resp.close()

# 查看浏览器的抓包中的.ts文件，可以看到现在的url是需要进行拼接
# 请求 URL: https://cdn7.caoliqi.com:65/20220708/3pwt0JO3/1215kb/hls/qjMM5WuJ.ts
# 拼接所需要的是https://cdn7.caoliqi.com:65 网站前缀
# 和上面得到m3u8_url前两步相同
pre_url = url.split('=')[1].rsplit('/', 3)[0]


with open('easy.m3u8', 'r') as f:
    index = 0
    for line in f:
        line = line.strip()
        # 不需要井号开头的
        if (line.startswith("#")):
            continue
        # 完整.ts的url
        down_url = pre_url + line
        resp = req.get(down_url, headers=headers)
        with open(f'./video/easy/{index + 1}.ts', mode='wb') as f2:
            f2.write(resp.content)
        print(f"已完成{index + 1}")
        index = index + 1
        time.sleep(0.5)

