import os


def merge_tv():
    lst = []
    with open('xc.m3u8', mode='r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            # /20220708/3pwt0JO3/1215kb/hls/qjMM5WuJ.ts
            # 得到name qjMM5WuJ.ts
            name = 'xc/' + line.strip().rsplit('/', 1)[1]
            lst.append(name)
    s = '+'.join(lst)
    print(s)
    os.system(f'copy/b {s} xc.mp4')

if __name__ == '__main__':
    merge_tv()
