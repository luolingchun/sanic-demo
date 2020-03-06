# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2020/3/6 17:53
import time

import requests
from multiprocessing import Pool


def f(i):
    # r = requests.get("http://localhost:8000/v1/job")
    r = requests.get("http://127.0.0.1:5000/v1/job")
    print(i, r.text)


if __name__ == '__main__':
    s = time.time()
    pool = Pool(4)
    for i in range(100):
        pool.apply_async(func=f, args=(i,))

    pool.close()
    pool.join()
    t = time.time()
    print(t - s)
