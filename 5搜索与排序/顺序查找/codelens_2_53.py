"""有序列表数据while循环实现顺序查找"""
'''
@Time    : 2018/2/8 上午10:53
@Author  : scrappy_zhang
@File    : codelens_2_53.py
'''


def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False
    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1

    return found


if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(orderedSequentialSearch(testlist, 3))
    print(orderedSequentialSearch(testlist, 13))
