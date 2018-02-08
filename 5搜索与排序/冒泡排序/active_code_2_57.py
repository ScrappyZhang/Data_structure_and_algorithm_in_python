"""
短冒泡排序


若某一次没有数据交换，说明列表是有序的，无需再进行冒泡
"""
'''
@Time    : 2018/2/8 下午2:09
@Author  : scrappy_zhang
@File    : active_code_2_57.py
'''


def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist) - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                # 说明此次遍历，有顺序不对的项，设置exchanges为True；否则exchanges为False
                exchanges = True
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
        passnum = passnum - 1


if __name__ == '__main__':
    alist = [20, 30, 40, 90, 50, 70, 60, 80, 100, 110]
    shortBubbleSort(alist)
    print(alist)
