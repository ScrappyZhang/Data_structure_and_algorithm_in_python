"""
归并排序

递归算法，不断将列表拆分为一半。
如果列表为空或有一个项，则按定义（基本情况）进行排序。
如果列表有多个项，分割列表，并递归调用两个半部分的合并排序

归并排序算法本身O(nlogn)

本源代码由于采取列表切片操作，因此需要额外的切片复杂度；除此之外，合并操作也需要操作时间和空间

所以为了保证归并排序算法本身的复杂度，在递归调用时应该以子列表起始结束索引值来作为回传参数来降低算法复杂度。
"""
'''
@Time    : 2018/2/8 下午2:57
@Author  : scrappy_zhang
@File    : active_code_1_511.py
'''


def mergeSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        # 合并排序
        while i < len(lefthalf) and j < len(righthalf):
            # 从小到大排列，所有元素，谁小先排谁，直到把某个子列元素排完
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            # 当右子列先被排完，则直接将左子列剩余元素添加到合并列末尾
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            # 当左子列先被排完，则直接将左子列剩余元素添加到合并列末尾
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
    print("Merging ", alist)


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(alist)
    print(alist)
