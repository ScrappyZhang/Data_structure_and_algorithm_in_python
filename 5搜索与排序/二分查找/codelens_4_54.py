"""递归二分法查找有序列表"""

"""
二分法本身算法复杂度： O(log(n))
每次递归调用列表切片算法复杂度：O(k)

所以要想除去列表切片非算法复杂影响，可以在递归调用时传参为相应的起始结束索引，而不是切片列表
"""
'''
@Time    : 2018/2/8 上午10:53
@Author  : scrappy_zhang
@File    : codelens_4_54.py
'''


def binarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            return True
        else:
            if item < alist[midpoint]:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)


if __name__ == '__main__':
    testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42, ]
    print(binarySearch(testlist, 3))
    print(binarySearch(testlist, 13))
