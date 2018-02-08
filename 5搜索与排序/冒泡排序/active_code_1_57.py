"""冒泡排序"""

"""
    算法复杂度O(n^2)
"""
'''
@Time    : 2018/2/8 下午2:04
@Author  : scrappy_zhang
@File    : active_code_1_57.py
'''


def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


if __name__ == '__main__':
    alist = [54,26,93,17,77,31,44,55,20]
    bubbleSort(alist)
    print(alist)
