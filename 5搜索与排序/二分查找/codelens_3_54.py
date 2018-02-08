"""二分法查找有序列表"""

"""
算法复杂度： O(log(n))
"""
'''
@Time    : 2018/2/8 上午10:53
@Author  : scrappy_zhang
@File    : codelens_3_54.py
'''


def binarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
