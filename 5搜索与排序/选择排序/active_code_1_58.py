"""

选择排序

每次遍历将最大值放在合适的位置

算法复杂度O(n^2)，但列表元素要比冒泡法交换的次数减少
"""
'''
@Time    : 2018/2/8 下午2:24
@Author  : scrappy_zhang
@File    : active_code_1_58.py
'''


def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selectionSort(alist)
    print(alist)
