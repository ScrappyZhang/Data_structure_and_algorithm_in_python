"""
快速排序


快速排序使用分而治之来获得与归并排序相同的优点，而不使用额外的存储。

快速排序首先选择一个值，该值称为 枢轴值。
虽然有很多不同的方法来选择枢轴值，我们将使用列表中的第一项。
枢轴值的作用是帮助拆分列表。
枢轴值属于最终排序列表（通常称为拆分点）的实际位置，将用于将列表划分为快速排序的后续调用。

"""
'''
@Time    : 2018/2/8 下午5:23
@Author  : scrappy_zhang
@File    : active_code_1_512.py
'''


def quickSort(alist):
    # 快速排序
    quickSortHelper(alist, 0, len(alist) - 1)


def quickSortHelper(alist, first, last):
    # 快速排序递归调用
    if first < last:
        # 获取枢纽位置
        splitpoint = partition(alist, first, last)
        # 左子列
        quickSortHelper(alist, first, splitpoint - 1)
        # 右子列
        quickSortHelper(alist, splitpoint + 1, last)


def partition(alist, first, last):
    # 割裂
    pivotvalue = alist[first]  # 枢纽值

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            # 当左标记不大于右标记，并且左标记的值小于枢纽值时，移动左标记
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            # 当右标记不小于左标记，并且右标记的值不小于枢纽值时，移动右标记
            rightmark = rightmark - 1

        if rightmark < leftmark:
            # 当右标记小于左标记时，一轮快速排序完成
            done = True
        else:
            # 左右交换
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    # 一轮快速排序完成时，需要交换枢纽值和当前右标记的位置
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    # 返回枢纽值目前的位置，以便递归快速排序分割为两个列表
    return rightmark


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quickSort(alist)
    print(alist)
