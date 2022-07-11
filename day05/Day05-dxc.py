# from threading import Thread
#
#
# # 方法1
# def fun(id):
#     for i in range(100):
#         print('fun', id, i)
#
#
# if __name__ == '__main__':
#     # 参数不能直接在target=fun()传递，借助args
#     t1 = Thread(target=fun, args=('t1',))
#     t2 = Thread(target=fun, args=('t2',))
#     t1.start()
#     t2.start()
#     for i in range(100):
#         print('main', i)

# 方法2
# class D(Thread):
#     def __init__(self, id):
#         super().__init__()
#         self.id = id
#
#     def run(self):
#         for i in range(100):
#             print('t', self.id, i)
#
#
# if __name__ == '__main__':
#     t1 = D(1)
#     t2 = D(2)
#     t1.start()
#     t2.start()

# 线程池
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def fn(name):
    for i in range(100):
        print(name, i)


if __name__ == "__main__":
    # 创建线程池
    with ThreadPoolExecutor(50) as t:
        for i in range(100):
            t.submit(fn, name=f'线程{i}')
    print("线程全部完成")
