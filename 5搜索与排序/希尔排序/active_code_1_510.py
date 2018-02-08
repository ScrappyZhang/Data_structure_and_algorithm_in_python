"""
希尔排序(递减递增排序)

通过将原始列表分解为多个较小的子列表来改进插入排序，每个子列表使用插入排序进行排序。
*****************************
选择这些子列表的方式是希尔排序的关键
****************************


算法复杂度在 O(n) 和 O(n^2 ) 之间

希尔排序使用增量i（有时称为 gap），通过选择 i 个项的所有项来创建子列表
"""
'''
@Time    : 2018/2/8 下午2:40
@Author  : scrappy_zhang
@File    : active_code_1_510.py
'''


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount,
              "The list is", alist)

        sublistcount = sublistcount // 2


def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap

        alist[position] = currentvalue


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shellSort(alist)
    print(alist)
