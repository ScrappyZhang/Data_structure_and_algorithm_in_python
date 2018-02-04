"""
pop()与pop(i)的对比

pop(0) 是 O(n), pop()是 O(1)

"""
'''
@Time    : 2018/2/4 下午3:35
@Author  : scrappy_zhang
@File    : listing4.py
'''
from timeit import timeit
import matplotlib.pyplot as plt

pt = []
pz = []

for i in range(10000, 100001, 10000):
    x = list(range(i))
    popzero = timeit("x.pop(0)",
                     "from __main__ import x",
                     number=1000)
    popend = timeit("x.pop()",
                    "from __main__ import x",
                    number=1000)
    pt.append(popzero)
    pz.append(popend)

n = list(range(10000, 100001, 10000))
plt.plot(n, pt, '+')
plt.plot(n, pz, 'o')
plt.show()
