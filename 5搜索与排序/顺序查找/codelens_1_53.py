"""无序列表数据while循环实现顺序查找"""
'''
@Time    : 2018/2/8 上午10:53
@Author  : scrappy_zhang
@File    : codelens_1_53.py
'''


def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

if __name__ == '__main__':
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 13))