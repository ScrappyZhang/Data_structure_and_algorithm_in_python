"""
对比列表和字典的contains方法

列表O(n)
字典O(1)

"""
'''
@Time    : 2018/2/4 下午3:54
@Author  : scrappy_zhang
@File    : listing6.py
'''

from timeit import timeit
import matplotlib.pyplot as plt

import random

pt = []
ps = []
for i in range(1000, 20001, 2000):
    # 列表
    x = list(range(i))
    t = timeit("random.randrange(%d) in x" % i,
               "from __main__ import random,x",
               number=1000)
    pt.append(t)
    # 字典
    y = {j: None for j in range(i)}
    s = timeit("random.randrange(%d) in y" % i,
               "from __main__ import random,y",
               number=1000)
    ps.append(s)

n = list(range(1000, 20001, 2000))
plt.plot(n, pt, '+')
plt.plot(n, ps, 'o')
plt.show()
