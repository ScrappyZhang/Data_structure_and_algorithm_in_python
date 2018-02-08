"""

归并排序


不采用切片操作

但合并排序处需注意选择合适的排序

以及每次递归需要一个完整的alist，占用了大量的空间
"""
'''
@Time    : 2018/2/8 下午3:13
@Author  : scrappy_zhang
@File    : active_code_2_511.py
'''
import copy


def mergeSort(alist, index0, index1):
    print("Splitting ", alist[index0:index1])
    # print(index0, index1)
    mid = index0 + (index1 - index0 + 1) // 2
    if mid != index0 and mid != index1:
        left_index0, left_index1 = index0, mid
        right_index0, right_index1 = mid, index1

        mergeSort(alist, left_index0, left_index1)
        mergeSort(alist, right_index0, right_index1)

        i = left_index0
        j = right_index0
        # 合并排序
        while j < right_index1:
            while i < left_index1:
                if alist[j] < alist[i]:
                    index = j
                    temp = alist[j]
                    while index > i:
                        alist[index] = alist[index - 1]
                        index -= 1
                    alist[i] = temp
                    left_index1 += 1
                    break
                i += 1
            j += 1
    print("Merging ", alist[index0:index1])


if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    mergeSort(alist, 0, len(alist))
    print()
