import requests as req

# 梨视频
url = 'https://www.pearvideo.com/video_1765348'
# 获取视频id
vid = url.split('_')[1]
# 是在xhr中，异步请求
v_url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1765348&mrd=0.10915277937466228'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
    # 反爬链，说白了就是记录你是从哪一个网页跳转过来的
    # 与上面的url一致
    'Referer': url  # 'https://www.pearvideo.com/video_1765348'
}

resp = req.get(v_url, headers=headers)
resp.encoding = 'utf-8'
# 得到是json数据，是视频相关的信息
# print(resp.json())
# 得到json数据中，携带的视频原链接，
# 此链接并不能直接使用，
# 观察页面浏览器最终的源代码，定位到video标签，会发现两者的不同
# json中的：https://video.pearvideo.com/mp4/short/20220614/1657245404127-15895948-hd.mp4
# 源码中的：https://video.pearvideo.com/mp4/short/20220614/cont-1765348-15895948-hd.mp4
# 要以源码中的为准，将json中的重新拼接得到源码中的地址形式
# json中与源码不同的信息可以在json中找到，目前名称为'systemTime': '1657245404127'
# 而源码中，cont-后面的是视频的id，在上面已经提取
systemTime = str(resp.json()['systemTime'])
srcUrl = str(resp.json()['videoInfo']['videos']['srcUrl'])
v_srcUrl = srcUrl.replace(systemTime, 'cont-' + (str(vid)))
# 可以打印出地址，看能否访问
print(v_srcUrl)
# 保存视频 以二进制写入到本地
with open('video/lsp.mp4', mode='wb') as f:
    f.write(req.get(v_srcUrl).content)
