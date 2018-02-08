"""
插入排序

算法复杂度：O(n^2 )


它始终在列表的较低位置维护一个排序的子列表。
然后将每个新项 “插入” 回先前的子列表，使得排序的子列表称为较大的一个项




"""
'''
@Time    : 2018/2/8 下午2:31
@Author  : scrappy_zhang
@File    : active_code_1_59.py
'''


def insertionSort(alist):
    for index in range(1, len(alist)):

        currentvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currentvalue:
            # 移位操作只需要交换大约三分之一的处理工作
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currentvalue


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    insertionSort(alist)
    print(alist)
