"""生成一个从0开始的n个数字的列表"""
'''
@Time    : 2018/2/4 下午3:08
@Author  : scrappy_zhang
@File    : list0_n.py
'''
"""
使用 append 方法或拼接运算符。append 方法是 O（1)。 然而，拼接运算符是 O（k），其中 k 是要拼接的列表的大小


concat  0.8938536189962178 milliseconds         +
append  0.06884013299713843 milliseconds    append
comprehension  0.030426548997638747 milliseconds 列表表达式
list range  0.012032343976898119 milliseconds   列表数据类型
"""

from timeit import timeit


# timeit 模块旨在允许 Python 开发人员通过在一致的环境中运行函数并使用尽可能相似的操作系统的时序机制来进行跨平台时序测量。

def test1():
    l = []
    for i in range(1000):
        l = l + [i]


def test2():
    l = []
    for i in range(1000):
        l.append(i)


def test3():
    l = [i for i in range(1000)]


def test4():
    l = list(range(1000))


t1 = timeit("test1()", "from __main__ import test1", number=1000)
print("concat ", t1, "milliseconds")
t2 = timeit("test2()", "from __main__ import test2", number=1000)
print("append ", t2, "milliseconds")
t3 = timeit("test3()", "from __main__ import test3", number=1000)
print("comprehension ", t3, "milliseconds")
t4 = timeit("test4()", "from __main__ import test4", number=1000)
print("list range ", t4, "milliseconds")


