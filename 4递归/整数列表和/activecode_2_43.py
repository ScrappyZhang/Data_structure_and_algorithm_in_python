"""

计算整数列表和

通过递归实现

列表 numList 的和是列表的第一个元素numList[0] 和列表其余部分numList [1:] 之和的总和。
"""

"""
该逻辑不是循环;递归的逻辑是通过将问题分解成更小和更容易的问题来解决的优雅表达。
"""
'''
@Time    : 2018/2/5 下午2:28
@Author  : scrappy_zhang
@File    : activecode_2_43.py
'''


def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + listsum(numList[1:])


print(listsum([1, 3, 5, 7, 9]))
